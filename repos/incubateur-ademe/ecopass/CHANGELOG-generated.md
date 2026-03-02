## Changelog : ecopass (30 derniers jours)

### Résumé
Les dernières mises à jour d'Ecopass se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec une nouvelle page de connexion et des améliorations de la page de déclaration. Des corrections de bugs ont été implémentées pour assurer la stabilité de la plateforme, et de nouvelles fonctionnalités ont été ajoutées pour permettre la création d'utilisateurs, la gestion du cycle de vie des produits et la délégation sans numéro SIRET.

### Évolutions fonctionnelles
- Nouvelle page de connexion pour une meilleure expérience utilisateur. [#120](https://github.com/incubateur-ademe/ecopass/issues/120)
- Amélioration de la page de déclaration des produits. [#121](https://github.com/incubateur-ademe/ecopass/issues/121)
- Ajout d'une page de création d'utilisateurs. [#116](https://github.com/incubateur-ademe/ecopass/issues/116)
- Possibilité de déléguer des droits sans nécessiter un numéro SIRET. [#111](https://github.com/incubateur-ademe/ecopass/issues/111)
- Ajout de la gestion du cycle de vie des produits. [#115](https://github.com/incubateur-ademe/ecopass/issues/115)
- Mise à jour des images de la page d'accueil. [#114](https://github.com/incubateur-ademe/ecopass/issues/114)
- Amélioration de l'explication du processus de connexion par email.
- Ajout de produits anonymisés pour des besoins spécifiques. [#112](https://github.com/incubateur-ademe/ecopass/issues/112)
- Possibilité de déclarer des produits en batch (en lot). [#110](https://github.com/incubateur-ademe/ecopass/issues/110)
- Ajout d'une notice en anglais. [#109](https://github.com/incubateur-ademe/ecopass/issues/109)
- Mise à jour du contenu de l'email de bienvenue. [#108](https://github.com/incubateur-ademe/ecopass/issues/108)

### Évolutions techniques
- Correction du calcul de l'impact environnemental pour une meilleure précision. [#122](https://github.com/incubateur-ademe/ecopass/issues/122)
- Correction d'un bug d'éjection automatique (logout). [#119](https://github.com/incubateur-ademe/ecopass/issues/119)
- Correction d'un lien vers la version du produit. [#118](https://github.com/incubateur-ademe/ecopass/issues/118)
- Ajout de Maildev dans les workflows GitHub Actions pour faciliter le débogage des emails. [#117](https://github.com/incubateur-ademe/ecopass/issues/117)
- Correction de problèmes liés au seeding de la base de données.
- Correction d'un problème avec le score obligatoire pour les AD (Analyse de Données).
- Correction d'un problème d'affichage du score dans les tests unitaires.
- Correction d'une erreur de build.
- Correction de l'enum des statistiques anonymisées.
- Correction du slug de catégorie dans l'anonymisation.
- Correction d'un problème lié à l'identifiant unique.
- Correction d'un bug d'affichage de la marque dans l'API. [#107](https://github.com/incubateur-ademe/ecopass/issues/107)
- Amélioration du remplissage des informations depuis GS1. [#106](https://github.com/incubateur-ademe/ecopass/issues/106)
- Possibilité de créer des organisations sans numéro SIRET. [#105](https://github.com/incubateur-ademe/ecopass/issues/105)
- Interdiction des uploads récents pour éviter les conflits. [#100](https://github.com/incubateur-ademe/ecopass/issues/100)

### Autres changements
- Mise à jour de la cartographie des navigateurs de base.
- Suppression d'autres types de NAFF (Nomenclature des Activités Françaises). [#113](https://github.com/incubateur-ademe/ecopass/issues/113)
