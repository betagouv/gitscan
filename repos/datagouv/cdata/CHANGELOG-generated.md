## Changelog : cdata (30 derniers jours, au 24 juin 2026)

### Résumé
Les 30 derniers jours ont été marqués par une amélioration significative de l'expérience utilisateur, notamment au niveau de l'explorateur tabulaire, de la recherche et des visualisations de données. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la performance de l'application. Plusieurs améliorations techniques ont été réalisées, notamment concernant les tests et l'infrastructure CI/CD.

### Évolutions fonctionnelles
- **Explorateur tabulaire :** Améliorations et corrections de bugs pour une meilleure expérience utilisateur [#1070, #1127].
- **Recherche :**
    - Possibilité de personnaliser l'ordre de tri par défaut [#1114].
    - Annonce du nombre de résultats et possibilité de focus automatique sur les résultats [#1096].
    - Correction d'un problème de condition de course lors de l'annulation des requêtes [#1146].
    - Correction du problème de réinitialisation de la page lors du changement de type de recherche [#1148].
- **Visualisations :** Amélioration des graphiques [#1088] et correction d'un problème de CORS [#1116].
- **Notifications :** Ajout de la possibilité de marquer les notifications comme lues individuellement ou en masse [#1103, #1121].
- **API Dataservice :** Amélioration du visualiseur de réponse OpenAPI [#1100].
- **Réutilisation :** Amélioration de l'affichage de l'image de réutilisation à l'étape 3 [#1134].
- **Sujets (Topics) :** Ajout d'une page dédiée aux sujets [#1110].
- **Tableau de bord :** Correction d'une faute de frappe [#1143].
- **Activités :** Affichage de l'ID de la ressource impactée dans les activités [#1123].
- **Titres :** Possibilité d'utiliser le caractère 'p' dans les balises de titre [#1119].

### Évolutions techniques
- **Tests :**
    - Ajout de tests unitaires [#1136].
    - Ajout de tests E2E et sharding des tests E2E [#1139, #1152].
- **CI/CD :**
    - Suppression des exécutions dupliquées dans le CI [#1128].
    - Activation des exécutions de pull request pour les contributions externes [#1042].
    - Mise à jour des dépendances [#1105].
- **Infrastructure :** Utilisation de `NODE_ENV production` dans le Dockerfile [#1104].
- **Composants :** Mise à jour des composants en version 1.1.2 et 1.3 [#1101, #1150].
- **Harvest :** Utilisation de la nouvelle API Harvest [#1074].
- **Sentry :** Ajout de la configuration du serveur Sentry [#1126].

### Autres changements
- Suppression du fichier `components lockfile` [#1156].
- Suppression des couches dans le type de métadonnées WFS [#1140].
- Ajout d'un horodatage dans les logs [#1084].
- Correction d'un problème d'envoi des identifiants avec la nouvelle politique CORS [#1098].
- Correction de pages 404 [#1094].
- Correction d'un problème d'hydratation dans les métriques [#1135].
- Correction d'un problème de chemins d'accès manquants [#1144].
- Correction d'un problème d'état de l'ensemble de données créé lors du flux de publication [#1142].
- Correction d'un problème lié à la branche udata dans le CI [#1131].
- Suppression de la date de création et ajout de l'URL de base dans la barre latérale dataservice [#1117].
- Utilisation de l'URI QR code retourné par le backend pour l'authentification à deux facteurs [#1090].
