import React, { useMemo, useState } from "react";
import {
	Text,
	ScrollView,
	View,
	TouchableOpacity,
	Image,
	ImageBackground,
	TextInput,
} from "react-native";
import { MaterialIcons } from "@expo/vector-icons";
import styles from "../Styles/style";

import { useNavigation } from "@react-navigation/native";

import RadioGroup from "react-native-radio-buttons-group";

import * as ImagePicker from "expo-image-picker";
import * as FS from "expo-file-system";

const InputPage = (route, nav) => {
	const params = route.route.params;

	const navigation = useNavigation();

	const [hasGalleryPermission, setHasGalleryPermission] = useState(null);
	const [hasCameraPermission, setHasCameraPermission] = useState(null);

	const [image, setImage] = useState("");
	const [imageUri, setImageUri] = useState("");

	const [name, setName] = useState("");
	const [age, setAge] = useState(null);
	const [city, setCity] = useState("");

	const [formFilled, setFormFilled] = useState(false);

	const url = "http://192.168.23.122:5000/";



	const radioButtons = useMemo(
		() => [
			{ id: 1, label: "Male", value: "male", color: "#ef9595" },
			{ id: 2, label: "Female", value: "female", color: "#ef9595" },
			{
				id: 3,
				label: "Prefer Not to Say",
				value: "prefer not to say",
				color: "#ef9595",
			},
		],
		[]
	);

	const [gender, setGender] = useState("");

	const ValidateInputs = () => {
		setFormFilled(
			name !== "" &&
				age !== null &&
				age >= 0 &&
				age <= 100 &&
				gender !== "" &&
				city.length > 3
		);
	};

	const askPermission = async (permissionFor) => {
		if (permissionFor === "camera") {
			const permission =
				await ImagePicker.requestCameraPermissionsAsync();
			setHasCameraPermission(permission.status === "granted");
		} else if (permissionFor === "gallery") {
			const permission =
				await ImagePicker.requestMediaLibraryPermissionsAsync();
			setHasGalleryPermission(permission.status === "granted");
		}
	};

	const pickImage = async () => {
		if (hasGalleryPermission === false) {
			askPermission();
		}

		let result = await ImagePicker.launchImageLibraryAsync({
			mediaTypes: ImagePicker.MediaTypeOptions.Images,
			allowsEditing: true,
			base64: true,
			aspect: [4, 3],
			quality: 1,
		});

		if (!result.canceled) {
			setImage(result);
			setImageUri(result.assets[0].uri);
		}

		ValidateInputs();
	};

	const captureImage = async () => {
		if (hasCameraPermission === false) {
			askPermission();
		}

		let result = await ImagePicker.launchCameraAsync({
			mediaTypes: ImagePicker.MediaTypeOptions.Images,
			allowsEditing: true,
			base64: true,
			aspect: [4, 3],
			quality: 1,
		});

		if (!result.canceled) {
			setImage(result);
			setImageUri(result.assets[0].uri);
		}
	};

	// const uploadImage = async () => {
	// 	let response = await FS.uploadAsync(
	// 		url + params.path,
	// 		image.assets[0].uri,
	// 		{
	// 			headers: {
	// 				"content-type": "image/jpeg",
	// 			},
	// 			httpMethod: "POST",
	// 			uploadType: FS.FileSystemUploadType.BINARY_CONTENT,
	// 		}
	// 	).catch((err) => console.error(err));
	// 	let val = JSON.parse(response.body);
	// 	val.ImageUri = imageUri;

	// 	// console.log(val);

	// 	navigation.navigate("OutputPage", val);
	// };

    const uploadImage = async () => {
        try {
            // Create a new FormData object
            let formData = new FormData();
    
            // Append the image file to the FormData object
            formData.append("image", {
                uri: image.assets[0].uri,
                type: "image/jpeg",
                name: "image.jpg",
            });
    
            // Append other form data as needed
            formData.append("city", city.trim());
            // formData.append("key2", "value2");
    
            // Send the FormData object as the body of the request
            let response = await fetch(url + params.path, {
                method: "POST",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "multipart/form-data",
                },
                body: formData,
            });
    
            // Parse the response
            let val = await response.json();
            val.ImageUri = imageUri;
    
            // Navigate to the output page with the response data
            navigation.navigate("OutputPage", val);
        } catch (err) {
            console.error(err);
        }
    };
    

	return (
		<ImageBackground
			source={require("../assets/background.jpg")}
			resizeMode="cover"
			style={{ flexGrow: 1 }}
		>
			<ScrollView
				automaticallyAdjustKeyboardInsets={true}
				contentContainerStyle={styles.container_col}
			>
				<View style={styles.container_col_flex_mt50}>
					<View style={styles.inputs_container}>
						<TextInput
							placeholder="Name"
							keyboardType="ascii-capable"
							style={styles.input}
							selectionColor={"#ef9595"}
							onChange={(val) => {
								setName(val.nativeEvent.text);
								ValidateInputs();
							}}
						/>

						<TextInput
							placeholder="Age"
							keyboardType="numeric"
							style={styles.input}
							selectionColor={"#ef9595"}
							onChange={(val) => {
								setAge(val.nativeEvent.text);
								ValidateInputs();
							}}
						/>

						<RadioGroup
							radioButtons={radioButtons}
							onPress={setGender}
							selectedId={gender}
							layout="row"
						/>
						<TextInput
							placeholder="City"
							style={styles.input}
							selectionColor={"#ef9595"}
							onChange={(val) => {
								setCity(val.nativeEvent.text);
								ValidateInputs();
							}}
						/>

						<View style={styles.container_row}>
							<TouchableOpacity
								onPress={captureImage}
								style={styles.button}
							>
								<MaterialIcons
									name="camera"
									size={24}
									color="#f1f1f1"
								/>
								<Text style={styles.buttonText}>
									Capture Image
								</Text>
							</TouchableOpacity>
							<TouchableOpacity
								onPress={pickImage}
								style={styles.button}
							>
								<MaterialIcons
									name="image"
									size={24}
									color="#f1f1f1"
								/>
								<Text style={styles.buttonText}>
									Pick Image
								</Text>
							</TouchableOpacity>
						</View>
					</View>
					<View>
						{imageUri !== "" ? (
							<Image
								source={{ uri: imageUri }}
								style={styles.image}
							/>
						) : (
							<></>
						)}
					</View>
					<TouchableOpacity
						onPress={uploadImage}
						style={
							formFilled && imageUri !== ""
								? styles.buttonL
								: styles.buttonL_disabled
						}
						disabled={formFilled && imageUri !== "" ? false : true}
					>
						<MaterialIcons
							name="search"
							size={50}
							color="#f1f1f1"
						/>
					</TouchableOpacity>
				</View>
			</ScrollView>
		</ImageBackground>
	);
};

export default InputPage;
