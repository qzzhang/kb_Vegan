/*
A KBase module: kb_Vegan
*/

module kb_Vegan {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /* Ref to a WS object
        @id ws
    */
    typedef string WSRef;

    /* An X/Y/Z style reference
    */
    typedef string obj_ref;

    /*
      A simple 2D matrix of floating point numbers with labels/ids for rows and
      columns.  The matrix is stored as a list of lists, with the outer list
      containing rows, and the inner lists containing values for each column of
      that row.  Row/Col ids should be unique.

      row_ids - unique ids for rows.
      col_ids - unique ids for columns.
      values - two dimensional array indexed as: values[row][col]
      @metadata ws length(row_ids) as n_rows
      @metadata ws length(col_ids) as n_cols
    */
    typedef structure {
        list<string> row_ids;
        list<string> col_ids;
        list<list<float>> values;
    } FloatMatrix2D;

    /*
      A wrapper around a FloatMatrix2D designed for simple matricies of MDS data.

      MDSMatrix Fields:
        description - short optional description of the dataset
        mds_parameters - arguments used to perform MDS analysis
        mds_output_items - important data items produced by the MDS analysis (including stress,converged,solution_reached, species,distance_metric,data and sample_scores)
        distance_matrix - (Bray_Curtis) distance matrix computed from the original_matrix
        rotation_matrix  - result rotation matrix
        original_matrix_ref - object reference to the original input (otu) matrix

        @optional description mds_parameters
        @optional distance_matrix mds_output_items

        @metadata ws length(rotation_matrix.row_ids) as otu_row_count
        @metadata ws length(rotation_matrix.col_ids) as sample_id_count
        @metadata ws original_matrix_ref as original_matrix_ref
    */
    typedef structure {
        string description;
        WSRef original_matrix_ref;
        mapping<string, string> mds_parameters;
        mapping<string, string> mds_output_items;
        FloatMatrix2D distance_matrix;
        FloatMatrix2D rotation_matrix;
    } MDSMatrix;

    /* Input of the run_mds function
        input_obj_ref: object reference to a KBaseMatrices matrix
        workspace_name: name of the workspace
        mds_matrix_name: name of MDS (KBaseExperiments.MDSMatrix) object (output)
        n_components - desired number of n dimensions is chosen for the ordination (default 2)
        metric - If True, perform metric MDS; otherwise, perform nonmetric MDS. (default False)
        max_iter - iterations stop once a set number of max_iter iterations have occurred (default 300)
        eps - relative tolerance with respect to stress at which to declare convergence (default 1e-3)
        distance_metric - distance the ordination will be performed on (Euclidean distance, Manhattan distance (city block distance) or Bray distance) default to Bray distance
        mds_ordination - can be rotated, inverted, or centered 

        attribute_mapping_obj_ref - associated attribute_mapping_obj_ref
        scale_size_by - used for MDS plot to scale data size
        color_marker_by - used for MDS plot to group data
    */
    typedef structure {
        obj_ref input_obj_ref;
        string workspace_name;
        string mds_matrix_name;
        int n_components;
        int max_iter;
        float eps;
        string distance_metric;
        string mds_ordination;
        obj_ref attribute_mapping_obj_ref;
        mapping<string, string> scale_size_by;
        mapping<string, string> color_marker_by;
    } MDSParams;

    /* Ouput of the run_mds function
        mds_ref: object reference (to an object of the MDSMatrix data type)
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
    */
    typedef structure {
        obj_ref mds_ref;
        string report_name;
        string report_ref;
    } MDSOutput;

    /* run_mds: perform MDS analysis on an input matrix*/
    funcdef run_mds (MDSParams params) returns (MDSOutput returnVal) authentication required;

};
