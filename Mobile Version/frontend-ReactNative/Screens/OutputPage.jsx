import {
	View,
	Text,
	Image,
	ScrollView,
	TouchableOpacity,
	ImageBackground,
} from "react-native";
import React from "react";
import styles from "../Styles/style";

import { MaterialIcons } from "@expo/vector-icons";
import { LinearGradient } from "expo-linear-gradient";
import { useNavigation } from "@react-navigation/native";

const OutputPage = (route) => {
	const params = route.route.params;

	const navigation = useNavigation();

	return (
		<ImageBackground
			source={require("../assets/background.jpg")}
			resizeMode="cover"
			style={{ flexGrow: 1 }}
		>
			<ScrollView>
				<Image
					source={{ uri: params.ImageUri }}
					style={styles.image_Sml}
				/>
				<Text style={styles.heading_text}>{params.DiseaseName}</Text>
				<Text style={styles.description}>{params.Description}</Text>

				{params.Tips.length > 0 ? (
					<Text style={styles.listHeading}>Tips :</Text>
				) : (
					<></>
				)}
				{params.Tips.length > 0 &&
					params.Tips.map((tip, i) => {
						return (
							<View key={i} style={styles.listContainer}>
								<Text style={styles.list}>
									{i + 1}. {tip}
								</Text>
							</View>
						);
					})}

				{params.FoodsToTake.length > 0 ? (
					<Text style={styles.listHeading}>Foods to Take :</Text>
				) : (
					<></>
				)}
				{params.FoodsToTake.length > 0 &&
					params.FoodsToTake.map((food, i) => {
						return (
							<View key={i} style={styles.listContainer}>
								<Text style={styles.list}>
									{i + 1}. {food}
								</Text>
							</View>
						);
					})}

				{params.FoodsNotToTake.length > 0 ? (
					<Text style={styles.listHeading}>Foods Not to Take :</Text>
				) : (
					<></>
				)}
				{params.FoodsNotToTake.length > 0 &&
					params.FoodsNotToTake.map((food, i) => {
						return (
							<View key={i} style={styles.listContainer}>
								<Text style={styles.list}>
									{i + 1}. {food}
								</Text>
							</View>
						);
					})}

				{params.Doctors.length > 0 ? (
					<Text style={styles.listHeading}>Recommended Doctors:</Text>
				) : (
					<></>
				)}
				{params.Doctors.map((doc, i) => (
					<View key={i} style={styles.listContainer}>
						<Text style={styles.list}>
						   <Text style={{fontWeight: "bold"}}>{i + 1}. {doc.name} {"\n"}</Text>	
							{doc.address}
						</Text>
					</View>
				))}

				{params.Warning ? (
					<Text style={styles.warningText}>{params.Warning[0]}</Text>
				) : (
					<></>
				)}

				<LinearGradient
					colors={["#df6283", "#d14646"]}
					style={styles.buttonHome}
				>
					<TouchableOpacity
						onPress={() => navigation.navigate("Get Started")}
					>
						<MaterialIcons name="home" size={30} color="#f1f1f1" />
					</TouchableOpacity>
				</LinearGradient>

				<Text style={styles.disclaimerText}>
					Disclaimer: This information is not intended to be a
					substitute for professional medical advice, diagnosis, or
					treatment. Always seek the advice of a qualified healthcare
					provider with any questions you may have regarding a medical
					condition.
				</Text>
			</ScrollView>
		</ImageBackground>
	);
};

export default OutputPage;
