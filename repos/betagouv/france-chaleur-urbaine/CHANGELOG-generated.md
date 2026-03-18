## Changelog : france-chaleur-urbaine (30 derniers jours, au 12 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du simulateur de chaleur, notamment avec l'intégration de données plus précises et une simplification de l'expérience utilisateur. Des améliorations techniques ont également été apportées pour faciliter la maintenance et l'évolutivité du projet, ainsi que la gestion des données réseaux de chaleur.

### Évolutions fonctionnelles
- **Simulateur :** Simplification du modèle de simulation et ajout de nouveaux modes de chauffage (Pac géo maison et Chaudière biomasse maison). [#1204](https://github.com/betagouv/france-chaleur-urbaine/pull/1204)
- **Simulateur :** Ajout d'une page méthodologie expliquant le fonctionnement du simulateur.
- **Simulateur :** Amélioration de l'affichage et de la réactivité sur mobile.
- **Adresse :** Implémentation d'un nouveau composant d'autocomplétion d'adresse pour une meilleure expérience utilisateur. [#1212](https://github.com/betagouv/france-chaleur-urbaine/pull/1212)
- **Données réseaux :** Mise à jour des données réseaux de chaleur avec les DLE 2024. [#1207](https://github.com/betagouv/france-chaleur-urbaine/pull/1207)
- **Formulaire de contribution :** Autorisation des fichiers PDF et vérification de l'intégrité des shapefiles pour les contributions de réseau. [#1209](https://github.com/betagouv/france-chaleur-urbaine/pull/1209)
- **Contact :** Remplacement de l'adresse email de contact par un formulaire. [#1208](https://github.com/betagouv/france-chaleur-urbaine/pull/1208)
- **Accessibilité :** Amélioration de l'accessibilité de la page d'accueil. [#1210](https://github.com/betagouv/france-chaleur-urbaine/pull/1210)
- **Affichage réseaux :** Les réseaux non ouverts sont maintenant affichés en gris.

### Évolutions techniques
- **API :** Refactorisation de l'appel à l'API de localisation avec `trpc`.
- **Base de données :** Nettoyage de la base de données (suppression de tables/colonnes inutilisées). [#1213](https://github.com/betagouv/france-chaleur-urbaine/pull/1213)
- **Tests :** Ajout de tests automatisés pour la BAN (Base Adresse Nationale).
- **PostHog :** Intégration de PostHog pour le suivi analytics et l'autocapture. [#1203](https://github.com/betagouv/france-chaleur-urbaine/pull/1203) et [#1211](https://github.com/betagouv/france-chaleur-urbaine/pull/1211)
- **Publicodes :** Mise à jour de la version de la librairie Publicodes.
- **Déploiement :** Ajout d'une option pour désactiver les clés étrangères lors de la création de dumps de la base de données.
- **Batenr :** Ajout de la gestion des données Batenr et de scripts pour leur importation.
- **Refactoring :** Refactorisation du code pour une meilleure organisation et maintenabilité.

### Autres changements
- **Documentation :** Mise à jour de la documentation de développement et des étapes de lancement du serveur.
- **Configuration :** Amélioration de la configuration de Knip et suppression du code mort.
- **Scripts :** Ajout d'un script pour remplir la table `communes_avec_ppa`.
- **Styles :** Divers ajustements de styles pour améliorer l'apparence et la réactivité de l'interface utilisateur.
- **Airtable :** Ajout d'informations supplémentaires dans les entrées Airtable (URL de simulation, date).
