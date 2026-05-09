## Changelog : Docurba (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, Docurba a bénéficié d'améliorations significatives concernant l'interface utilisateur, notamment une refonte du menu d'authentification et l'ajout d'une bannière d'information sur la page de connexion. Des améliorations ont également été apportées à l'API et aux données, avec l'ajout de nouvelles informations sur les procédures et les communes, ainsi que des corrections pour assurer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Authentification:** Refonte du menu d'authentification avec un menu déroulant pour l'utilisateur, incluant un bouton vers le tableau de bord. [#1868](https://github.com/MTES-MCT/Docurba/issues/1868)
- **Page de connexion:** Ajout d'une bannière d'information pour les utilisateurs non authentifiés, clarifiant le processus de création de compte. [#1865](https://github.com/MTES-MCT/Docurba/issues/1865)
- **Navigation:** Correction d'un problème de lien et amélioration de la synchronisation des filtres lors du changement de département.
- **API:** Exposition des sujets des procédures dans l'API SCOT et des communes.
- **Données:** Ajout d'un champ pour indiquer si une procédure a débuté avant la loi Huwart et documentation du type de procédure.

### Évolutions techniques
- **Tests:** Amélioration des tests de l'API SCoT et ajout de factories pour faciliter la création d'objets de test (Event, Collectivite, User, Profile, Procedure, CommuneProcedure).
- **Infrastructure:** Augmentation de la taille du disque et du plan Supabase pour les applications de revue afin de corriger les erreurs de mémoire récurrentes.
- **CI/CD:** Déploiement des serveurs horaire pour nettoyer la mémoire plus souvent.
- **Backend:** Correction d'un problème empêchant la restauration des migrations Django et ajout d'une classe d'index personnalisée pour gérer les index surdimensionnés.
- **Outils:** Mise à jour de plusieurs dépendances : `pre-commit`, `ruff`, `pytest`, `django-debug-toolbar`, `django`.
- **Makefile:** Mise à jour du Makefile pour améliorer la gestion des sources et suppression de l'activation de l'environnement virtuel dans les tâches de test.
- **Code:** Suppression du module de création d'objets de test et correction de problèmes SonarQube.

### Autres changements
- **Documentation:** Mise à jour de la documentation de l'API Nuxt pour inclure les nouveaux sujets des communes et des SCOT.
- **README:** Correction d'une erreur dans l'outil mentionné dans le README.
- **Style:** Utilisation des couleurs du thème Vuetify au lieu de CSS personnalisés pour la bannière de connexion.
- **Wording:** Mise à jour de la formulation sur la bannière de connexion.
