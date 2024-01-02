#!/bin/bash
# ========================================
#  Download OpenPack (v1.0.0) from Zenodo
# ========================================
OPENPACK_VERSION="v1.0.0"
BASE_URL=https://zenodo.org/records/8145223

DATASET_ROOTDIR=$1
OPENPACK_ROOTDIR="${DATASET_ROOTDIR%/}/openpack/${OPENPACK_VERSION}"
ZENODO_ZIP_DIR="${OPENPACK_ROOTDIR}/zenodo"

ZIP_FILE_LIST=(
    "preprocessed preprocessed-IMU-with-operation-labels.zip"
    "U0101 U0101.zip"
    "U0102 U0102.zip"
    "U0103 U0103.zip"
    "U0104 U0104.zip"
    "U0105 U0105.zip"
    "U0106 U0106.zip"
    "U0107 U0107.zip"
    "U0108 U0108.zip"
    "U0109 U0109.zip"
    "U0110 U0110.zip"
    "U0111 U0111.zip"
    "U0201 U0201.zip"
    "U0202 U0202.zip"
    "U0203 U0203.zip"
    "U0204 U0204.zip"
    "U0205 U0205.zip"
    "U0206 U0206.zip"
    "U0207 U0207.zip"
    "U0208 U0208.zip"
    "U0209 U0209.zip"
    "U0210 U0210.zip"
)


# == Check Parameters ==
if [ -z $DATASET_ROOTDIR ]; then
    echo "Required argument DATASET_ROOTDIR is missing."
    echo "Usage:"
    echo "    bash ./download_zenodo.sh <path to a dataset root directory>"
    exit 1
fi
if [ ! -d $DATASET_ROOTDIR ]; then
    echo "DATASET_ROOTDIR=${DATASET_ROOTDIR} does not exists. Please make it before."
    exit 1
fi

# == Prepare Download Directory  ==
echo "Download OpenPack dataset (${OPENPACK_VERSION}) into ${OPENPACK_ROOTDIR}."
if [ -d $OPENPACK_ROOTDIR ]; then
    echo "Directory (${OPENPACK_ROOTDIR}) already exists."
    read -p "  Do you want to overwrite this directory? (y/n): " continue_execution

    # Continue if the response is "y" or "Y"
    if [ "$continue_execution" == "y" ] || [ "$continue_execution" == "Y" ]; then
        echo "  Continue ..."
    else
        echo "  Abort"
        exit 1
    fi
else
    echo "makdir: ${OPENPACK_ROOTDIR}"
    mkdir -p $OPENPACK_ROOTDIR
    if [ $? -ne 0 ]; then
        echo "Failed to make directory: ${OPENPACK_ROOTDIR}"
        exit 1
    fi
fi

echo "makdir: ${ZENODO_ZIP_DIR}"
mkdir -p ${ZENODO_ZIP_DIR}
if [ $? -ne 0 ]; then
    echo "Failed to make directory: ${ZENODO_ZIP_DIR}"
  exit 1
fi


# == Download and Unzip Dataset ==
echo "Download data from zenodo."
for subdir_and_file_name in "${ZIP_FILE_LIST[@]}"; do
    subdir_and_file_name=($subdir_and_file_name)
    subdir=${subdir_and_file_name[0]}
    file_name=${subdir_and_file_name[1]}
    echo "  ${file_name}"

    download_url="${BASE_URL}/files/${file_name}?download=1"
    download_path="${ZENODO_ZIP_DIR}/${file_name}"
    echo "    Download from ${download_url} to ${download_path}"
    curl -L -o "${download_path}" "$download_url"

    echo "    Unzip ${download_path} to ${OPENPACK_ROOTDIR}/${subdir}"
    unzip "${download_path}" -d "${OPENPACK_ROOTDIR}/${subdir}"

    echo "    Done!"
done

echo "The OpenPack data set (${OPENPACK_VERSION}) was successfully downloaded!"
