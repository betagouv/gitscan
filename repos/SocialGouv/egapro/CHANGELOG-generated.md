## Changelog : egapro (30 derniers jours, au 2026-07-30)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur, notamment la correction de bugs affectant l'affichage, la soumission des données et la navigation. Des améliorations techniques ont également été apportées pour faciliter le déploiement, la gestion des environnements et la qualité du code. L'ajout du numéro de version dans le footer permet une meilleure identification de la version utilisée.

### Évolutions fonctionnelles
- Ajout du numéro de version dans le footer de l'application. [#4047](https://github.com/SocialGouv/egapro/issues/4047)
- Correction de l'alignement de l'alerte "Prochaines étapes" avec l'indicateur G. [#4049](https://github.com/SocialGouv/egapro/issues/4049)
- Correction du dénominateur des proportions variable H/F dans la déclaration. [#4048](https://github.com/SocialGouv/egapro/issues/4048)
- Amélioration de l'affichage des écarts, désormais tronqués à deux décimales. [#4039](https://github.com/SocialGouv/egapro/issues/4039)
- Rendre le seuil de 5% symétrique pour une meilleure interprétation. [#4040](https://github.com/SocialGouv/egapro/issues/4040)
- Masquage de la section CSE lorsque aucun avis n'est attendu. [#4032](https://github.com/SocialGouv/egapro/issues/4032)
- Correction du parcours "justification des écarts" sans CSE. [#4027](https://github.com/SocialGouv/egapro/issues/4027)
- Correction des accordéons inutilisables après suppression puis ré-import de données. [#4025](https://github.com/SocialGouv/egapro/issues/4025)
- Correction de la deadline de la déclaration 2 en phase 2 et ré-envoi de la 2nde déclaration depuis l'état "en attente de choix". [#4003](https://github.com/SocialGouv/egapro/issues/4003)
- Amélioration de l'affichage du bandeau entreprise et de l'étape de la démarche "Représentation". [#4024](https://github.com/SocialGouv/egapro/issues/4024)
- Correction de l'affichage des bordures des cases à cocher et des radios sous Firefox. [#4026](https://github.com/SocialGouv/egapro/issues/4026)
- Prévention du téléchargement multiple de PDF en cas de clics répétés. [#4019](https://github.com/SocialGouv/egapro/issues/4019)
- Correction de l'affichage du panneau latéral en fonction de la taille et du flag CSE. [#4000](https://github.com/SocialGouv/egapro/issues/4000)
- Correction de la position des caractères combinants dans les polices embarquées des PDF. [#4018](https://github.com/SocialGouv/egapro/issues/4018)
- Blocage de la soumission du formulaire si les champs de rémunération sont manquants pour un effectif non nul. [#4002](https://github.com/SocialGouv/egapro/issues/4002)
- Ajout de la source des catégories d'emplois en libellé lisible dans le PDF. [#4016](https://github.com/SocialGouv/egapro/issues/4016)
- Message d'erreur CSE plus explicite en français dans le bandeau informations manquantes. [#3997](https://github.com/SocialGouv/egapro/issues/3997)
- Ajout du bouton "Je donne mon avis" en fin de parcours. [#3966](https://github.com/SocialGouv/egapro/issues/3966)
- Implémentation des règles d'envoi et du contenu des emails de rappel. [#3857](https://github.com/SocialGouv/egapro/issues/3857)
- Ajout du bouton d'export dans l'étape 5 (indicateur G). [#3968](https://github.com/SocialGouv/egapro/issues/3968)
- Correction de l'affichage de la vraie proportion de bénéficiaires (étape 6 + PDF). [#3869](https://github.com/SocialGouv/egapro/issues/3869)

### Évolutions techniques
- La promotion bake la version dans l'image (app_version).
- Les envs de test persistants déploient une image versionnée.
- Correction d'un bug empêchant l'import GIP d'attendre la fin du rollout. [#4058](https://github.com/SocialGouv/egapro/issues/4058)
- Refactor du moteur d'étapes FSM avec un verrou compilateur. [#3979](https://github.com/SocialGouv/egapro/issues/3979)
- Dérivation du vocabulaire de statut admin de `DECLARATION_FSM_STATUSES`. [#3983](https://github.com/SocialGouv/egapro/issues/3983)
- Amélioration du workflow de release avec un canal prerelease alpha. [#3799](https://github.com/SocialGouv/egapro/issues/3799)
- Migration des builds d'images de buildkit-service vers buildkit-operator. [#3844](https://github.com/SocialGouv/egapro/issues/3844)
- Correction des permissions OIDC manquantes sur le workflow de promotion des envs de test. [#3908](https://github.com/SocialGouv/egapro/issues/3908)
- Correction d'un bug de création de tag lié au signage GPG. [#3906](https://github.com/SocialGouv/egapro/issues/3906)
- Création d'environnements de test persistants déployables uniquement depuis des releases. [#3904](https://github.com/SocialGouv/egapro/issues/3904)
- Correction d'un bug de protection de branche sur le canal prerelease alpha. [#3905](https://github.com/SocialGouv/egapro/issues/3905)

### Autres changements
- Documentation du changelog IA exhaustif. [#4046](https://github.com/SocialGouv/egapro/issues/4046)
- Mise à jour de la documentation concernant l'utilisation de Claude pour l'analyse des bugs. [#3995](https://github.com/SocialGouv/egapro/issues/3995)
- Amélioration de la nomenclature des cas de tests. [#4006](https://github.com/SocialGouv/egapro/issues/4006)
- Ajout de colonnes "Start date" et "End date" au board d'orchestration. [#3990](https://github.com/SocialGouv/egapro/issues/3990)
- Élagage des tests subsumés par le verrou FSM et la table de décision. [#3987](https://github.com/SocialGouv/egapro/issues/3987)
- Ajout de la purge des données des déclarations. [#3828](https://github.com/SocialGouv/egapro/issues/3828)
- Implémentation du système d'accessibilité Ultra11y. [#3887](https://github.com/SocialGouv/egapro/issues/3887)
- Amélioration de la discipline de fidélité Figma. [#3961](https://github.com/SocialGouv/egapro/issues/3961)
