**convert model to IR format**
if you have install openvino use below command or install openvino toolkit


python /home/faizan/intel/openvino_2020.1.023/deployment_tools/model_optimizer/mo_tf.py --input_model 8_exported_model/frozen_inference_graph.pb --output_dir 10_convert_model_to_IR/ --tensorflow_use_custom_operations_config /home/faizan/intel/openvino_2020.1.023/deployment_tools/model_optimizer/extensions/front/tf/ssd_support_api_v1.14.json --tensorflow_object_detection_api_pipeline_config 8_exported_model/pipeline.config --input_shape [1,300,300,3] --data_type FP16