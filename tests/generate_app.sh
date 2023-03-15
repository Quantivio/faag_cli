#pip install -e .

mkdir test_directory

# shellcheck disable=SC2164
cd test_directory

faag generate

rm -rf app

# shellcheck disable=SC2103
cd ..

rm -rf test_directory
