#pip install -e .

mkdir test_directory && cd test_directory

faag generate

rm -rf app

cd ..

rm -rf test_directory