import { View, Text, TouchableOpacity, ImageBackground, Image, Dimensions } from "react-native";
import styles from "../Styles/style";
import { useNavigation } from "@react-navigation/native";

import { LinearGradient } from "expo-linear-gradient";

const GetStartedPage = () => {
	const navigation = useNavigation();
    const win = Dimensions.get('window');

	return (
		<ImageBackground
			source={require("../assets/background.jpg")}
			resizeMode="cover"
			style={styles.container_col_flex}
		>
			<View>
            <Image source={require('../assets/FirstPage.png')} style={{width:win.width/1, height:win.height/2, resizeMode: 'contain',marginBottom: 15}} />
				<Text style={styles.heading_text}>Derm Lens</Text>
				<Text style={styles.subHeadingPhrase}>
					Let's Check your Skin...
				</Text>
			</View>

			<LinearGradient
				colors={["#df6283", "#d14646"]}
				style={styles.button}
			>
				<TouchableOpacity
					onPress={() => navigation.navigate("SelectionPage")}
				>
					<Text style={styles.buttonText}>Get Started &rarr;</Text>
				</TouchableOpacity>
			</LinearGradient>
		</ImageBackground>
	);
};

export default GetStartedPage;
