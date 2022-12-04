from pmu_breaking.ml_logic.Model1.v1_edouard_preprocessing import to_df, clean_data, refining_target, define_features_target, scaling_imputing
from pmu_breaking.ml_logic.Model1.model import test_pred,initialize_model, train_model, evaluate_model, test_pred
from pmu_breaking.ml_logic.Model1.model import save_model, predict_from_saved_model

if __name__ == '__main__':
    clean_data()
    to_df()
    scaling_imputing()
    initialize_model(),
    train_model()
    evaluate_model()
    test_pred()
    predict_from_saved_model()
    predict_from_saved_model()
    # save_model()
    # predict_from_saved_model()
