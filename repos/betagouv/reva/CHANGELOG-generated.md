## Changelog : reva (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations de l'expérience utilisateur, notamment avec l'intégration de FranceConnect pour la connexion et l'inscription, ainsi que par la refonte des pages de connexion et d'inscription. Des améliorations ont également été apportées à la génération de documents (DFF) et à l'administration, notamment pour la gestion des cohortes VAE collectives. Des corrections de bugs et des optimisations techniques ont également été réalisées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Intégration de FranceConnect pour l'inscription et la connexion des utilisateurs (#1123, #1124, #1125).
- Refonte complète des pages de connexion et d'inscription avec une nouvelle interface utilisateur (#1126, #1127, #1128).
- Amélioration du processus de création de candidature via FranceConnect (#1129, #1130).
- Ajout d'une confirmation modale pour la validation de la complétude des certifications par les autorités de certification (#1131).
- Amélioration de l'affichage des résultats de jury dans l'interface d'administration (#1132).
- Ajout d'une fonctionnalité permettant de sélectionner plusieurs certifications pour les cohortes VAE collectives (#1133, #1134).
- Ajout d'une section "Contacts" et "Avis et documents" dans la génération des documents DFF dématérialisés (#1135, #1136).
- Ajout d'une section "Accompagnement proposé au candidat" dans la génération des documents DFF dématérialisés (#1137).
- Amélioration de l'affichage des informations d'adresse dans le formulaire de contact (#1138).

### Évolutions techniques
- Refactorisation du code pour améliorer la gestion des erreurs et la sécurité, notamment avec l'implémentation de cookies sécurisés et de la gestion des tokens (#1139, #1140).
- Mise à jour des dépendances pour améliorer la performance et la sécurité (#1141, #1142, #1143, #1144, #1145, #1146, #1147).
- Génération automatique des types GraphQL pour assurer la compatibilité entre les différentes parties de l'application (#1148, #1149).
- Amélioration de la gestion des variables d'environnement et des configurations (#1150, #1151).
- Ajout de tests unitaires et d'intégration pour améliorer la qualité du code (#1152, #1153, #1154).
- Refactorisation de l'architecture pour simplifier le code et améliorer la maintenabilité (#1155, #1156, #1157, #1158, #1159, #1160, #1161).

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés (#1162).
- Correction de bugs mineurs et améliorations de l'interface utilisateur (#1163, #1164, #1165, #1166, #1167).
- Ajout de fichiers de configuration pour améliorer la gestion des projets (#1168).
- Nettoyage du code et suppression de code obsolète (#1169).
- Correction de problèmes de responsive design sur la page FAQ (#1170).
- Ajout de tests pour la nouvelle fonctionnalité de sélection de certifications en VAE collective (#1171).
- Ajout d'un feature flag pour activer la possibilité d'enregistrer un compte avec un mot de passe (#1172).
