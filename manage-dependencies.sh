while read p; do
  pip install --force-reinstall $p
done < dependencies
