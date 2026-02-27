## Changelog : eva-serveur (30 derniers jours)

### Résumé
Les dernières mises à jour d'eva-serveur se concentrent sur l'amélioration de l'expérience utilisateur, notamment pour les comptes EvaPro, avec une refonte du tableau de bord, l'ajout de fonctionnalités spécifiques (gestion des usages, validation SIRET, affichage du logo de l'OPCO), et des corrections de bugs. Des améliorations techniques ont également été apportées, notamment des mises à jour de dépendances et des optimisations de code.

### Évolutions fonctionnelles
- Les utilisateurs peuvent rejoindre une structure existante EVA même si elle n'existe pas sur l'API Officielle. (#893fecd)
- Ajout de la liste des IDCC dans les informations des OPCO. (#4b79713)
- Amélioration de la mise en page des sections d'évaluation et des mesures clés pour une meilleure présentation sur mobile. (#50babe6, #5c19201)
- Le tableau de bord est maintenant responsive. (#8bdce38)
- Génération d'un code campagne même si la structure n'a pas de code postal. (#16db37b)
- Les utilisateurs EvaPro peuvent modifier toutes leurs informations. (#22d820a)
- Affichage du logo de l'OPCO financeur dans le footer et sur le résultat d'une évaluation. (#9dd750b, #d272749)
- Ajout de la possibilité de télécharger le rapport PDF d'une évaluation EvaPro. (#c82b53d, #16ad7b5, #2dec6c7, #9689f25)
- Ajout d'un champ URL de contact pour les OPCO, modifiable par l'administrateur. (#0dcb385, #d516853, #bb0eb73)
- Ajout de la gestion des usages dans le processus d'inscription. (#4ae7cd7, #9b6661f)
- Ajout de la validation du SIRET et affichage d'une erreur si le SIRET est invalide. (#8cb0a70, #cf438e8)
- Les superadmins peuvent déplacer le dernier administrateur d'une structure. (#993f22a)
- Ajout de questionnaires supplémentaires pour Bienvenue, avec une option pour les questions de santé. (#b70e25c, #a43e9b0, #797c4e3)

### Évolutions techniques
- Refactorisation du code pour séparer les vues d'évaluation entre EVA et EvaPro. (#956bfcf)
- Suppression du modèle `StructureOpco` et simplification de la relation entre les structures et les OPCO. (#728f9ac, #5a5ca5f)
- Ajout d'un linter pour garantir la qualité du code. (#572b67a, #4129b11, #d0f0008)
- Mise à jour du Design System Fr (DSFR) de la version 1.13.0 à la version 1.14.2. (#2712418)
- Optimisation de la CI. (#4691b96)
- Utilisation du composant `BoutonDsfr` pour une gestion améliorée des boutons. (#3f49950, #68e9f36)
- Suppression de code inutile. (#11a485f, #edda441)
- Mise à jour des dépendances : `rack`, `faraday`, `nokogiri`. (#9319244, #22f96f5, #223e908)

### Autres changements
- Déplacement des logos dans un dossier `logos`. (#b879a18)
- Correction de la redirection après la connexion pour une structure. (#07df81b)
- Correction de l'affichage des risques et des coups. (#581fe5d)
- Amélioration de la mise en page de la page de connexion. (#6bda929, #0710403)
- Ajout de tests pour le helper `Admin::DashboardHelper`. (#c2d0275)
- Documentation de la variable d'environnement `ACTIVE_EVAPRO`. (#98870ee)
- Suppression de la configuration Mailjet pour le tracking. (#9ab6c80)
- Correction de bugs mineurs et améliorations de la typographie et du style.
