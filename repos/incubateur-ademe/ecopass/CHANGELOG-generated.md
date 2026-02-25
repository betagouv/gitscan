## Changelog : ecopass (30 derniers jours)

### Résumé
Les dernières mises à jour d'Ecopass se concentrent sur l'amélioration de l'expérience utilisateur, notamment en facilitant la création de comptes, la déclaration de produits et la gestion des organisations. Des corrections de bugs ont également été apportées pour assurer la stabilité de la plateforme et l'exactitude des données. De nouvelles fonctionnalités ont été implémentées pour permettre la délégation sans SIRET et l'anonymisation des produits.

### Évolutions fonctionnelles
- Ajout d'une page de création d'utilisateur (#116).
- Correction d'un bug empêchant l'affichage du score dans l'interface utilisateur.
- Correction d'un problème de lien vers la version du produit (#118).
- Implémentation d'une déconnexion automatique après une période d'inactivité (#119).
- Ajout du cycle de vie d'un produit (#115).
- Amélioration de l'explication concernant la connexion par email.
- Possibilité de déléguer sans SIRET (#111).
- Autorisation de la déclaration groupée de produits en production (#110).
- Ajout d'un avis en anglais (#109).
- Correction d'une erreur d'affichage de la marque dans l'API (#107).
- Ajout d'informations supplémentaires issues de GS1 (#106, #104, #103).
- Ajout de produits anonymisés (#112).

### Évolutions techniques
- Intégration de Maildev dans les actions GitHub pour faciliter les tests d'envoi d'emails (#117).
- Correction d'un problème de build.
- Correction de problèmes liés au seeding de la base de données.
- Correction d'un problème d'énumération des statistiques anonymisées.
- Correction d'un bug lié à la suppression d'autres NAFs (#113).
- Correction d'un problème de slug de catégorie dans l'anonymisation.
- Empêchement du téléchargement récent de fichiers (#100).
- Correction d'un script Datagouv.
- Correction d'un problème d'affichage des statistiques indisponibles (#102).
- Mise à jour de l'email de bienvenue (#108).
- Possibilité de créer des organisations sans SIRET (#105).

### Autres changements
- Mise à jour de la cartographie du navigateur de base (chore).
- Correction d'un score obligatoire vide.
- Mise à jour des images de la page d'accueil (#114).
- Ajout d'un identifiant unique en texte.
- Remplissage d'informations supplémentaires provenant de GS1.
