for i in {1..30}
do
  echo "Number: $i"
  bash eval_dev.sh ~/CommonGen/methods/unilm_based/decoded_sentences/dev/model.$i.bin.dev > unilm_dev_res/unilm_dev_$i.res 
done