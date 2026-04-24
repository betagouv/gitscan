## Changelog : egapro (30 derniers jours, au 2026-04-23)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans l'espace personnel et l'administration, avec de nouvelles fonctionnalités de recherche, de navigation et de gestion des données. Des améliorations techniques ont également été apportées pour optimiser les performances, la sécurité et l'infrastructure, incluant l'ajout d'un cache Redis et la mise en place d'un système d'audit.

### Évolutions fonctionnelles
- Ajout d'un graphique de progression de campagne (statistiques) dans l'espace administrateur. [#3286](https://github.com/SocialGouv/egapro/issues/3286)
- Ajout d'un filtre par taille d'entreprise. [#3283](https://github.com/SocialGouv/egapro/issues/3283)
- Amélioration de l'interface de l'espace personnel : couleurs des étapes du panneau latéral et état du choix au second tour mis à jour. [#3207](https://github.com/SocialGouv/egapro/issues/3207) [#3280](https://github.com/SocialGouv/egapro/issues/3280)
- Pré-remplissage automatique des données de la déclaration à partir de la dernière déclaration (indicateur 7). [#3246](https://github.com/SocialGouv/egapro/issues/3246) [#3269](https://github.com/SocialGouv/egapro/issues/3269)
- Amélioration de la gestion du "mimoquage" (impersonation d'entreprise) : champs en lecture seule, navigation entre les étapes enregistrées, restauration de la bannière. [#3253](https://github.com/SocialGouv/egapro/issues/3253)
- Suivi de la finalisation de l'avis du CSE avec un horodatage dédié. [#3271](https://github.com/SocialGouv/egapro/issues/3271)
- Ajout d'un lien vers les déclarations dans le menu latéral de l'espace administrateur. [#3275](https://github.com/SocialGouv/egapro/issues/3275)
- Ajout de la possibilité de rechercher des référents (personnes habilitées) et d'accéder à une page de recherche publique. [#3186](https://github.com/SocialGouv/egapro/issues/3186) [#3234](https://github.com/SocialGouv/egapro/issues/3234)
- Ajout d'une attestation de non-sanction (au format PDF). [#3089](https://github.com/SocialGouv/egapro/issues/3089)
- Amélioration de l'affichage du nombre total de salariés dans l'étape 5 de la déclaration. [#3160](https://github.com/SocialGouv/egapro/issues/3160) [#3163](https://github.com/SocialGouv/egapro/issues/3163)
- Ajout de la possibilité d'éditer les variables globales de campagne dans l'espace administrateur. [#3229](https://github.com/SocialGouv/egapro/issues/3229)
- Ajout de la gestion des référents (CRUD, import/export, API publique) dans l'espace administrateur. [#3198](https://github.com/SocialGouv/egapro/issues/3198)
- Ajout de la possibilité d'exporter les fichiers CSE (avis et évaluation conjointe) dans l'API. [#2905](https://github.com/SocialGouv/egapro/issues/2905) [#3200](https://github.com/SocialGouv/egapro/issues/3200)
- Ajout d'une page de recherche multi-critères pour les déclarations dans l'espace administrateur. [#3196](https://github.com/SocialGouv/egapro/issues/3196)
- Ajout d'une navigation via un menu latéral dans l'espace administrateur. [#3195](https://github.com/SocialGouv/egapro/issues/3195)

### Évolutions techniques
- Ajout d'une passerelle API. [#3304](https://github.com/SocialGouv/egapro/issues/3304)
- Mise en place d'une couche de cache Valkey Redis-compatible pour Next.js. [#3228](https://github.com/SocialGouv/egapro/issues/3228)
- Mise en place d'un système d'audit logging avec instrumentation des actions utilisateurs. [#3191](https://github.com/SocialGouv/egapro/issues/3191) [#3193](https://github.com/SocialGouv/egapro/issues/3193)
- Utilisation de Tipimail pour l'envoi d'emails en production. [#3237](https://github.com/SocialGouv/egapro/issues/3237) [#3238](https://github.com/SocialGouv/egapro/issues/3238)
- Ajout d'un sitemap.xml et d'un robots.txt pour le SEO. [#3235](https://github.com/SocialGouv/egapro/issues/3235)
- Refactorisation de la suppression des index et des filtres "Index" et "Valeur" dans l'espace administrateur. [#3276](https://github.com/SocialGouv/egapro/issues/3276)
- Refactorisation de la suppression du filtre de nom des référents dans l'espace administrateur et la recherche publique. [#3281](https://github.com/SocialGouv/egapro/issues/3281) [#3282](https://github.com/SocialGouv/egapro/issues/3282)
- Refactorisation de la base de données : aplatissement de la table `declaration_category` en colonnes d'indicateurs typées. [#3106](https://github.com/SocialGouv/egapro/issues/3106)
- Refactorisation de la liaison des tables CSE et évaluation conjointe à la déclaration. [#3111](https://github.com/SocialGouv/egapro/issues/3111)
- Refactorisation de la table `user` pour supprimer les colonnes redondantes. [#3122](https://github.com/SocialGouv/egapro/issues/3122)
- Mise en place d'un job Cron pour nettoyer les données d'audit en base de données. [#3270](https://github.com/SocialGouv/egapro/issues/3270)
- Ajout d'un certificat pour l'API privée SUIT. [#3120](https://github.com/SocialGouv/egapro/issues/3120)

### Autres changements
- Ajout de documentation de référence pour l'API SUIT. [#3284](https://github.com/SocialGouv/egapro/issues/3284)
- Correction d'un bug empêchant la soumission du formulaire "informations manquantes". [#3086](https://github.com/SocialGouv/egapro/issues/3086) [#3087](https://github.com/SocialGouv/egapro/issues/3087)
- Correction d'un bug lié à la copie-coller de texte traduit. [#2688](https://github.com/SocialGouv/egapro/issues/2688)
- Correction d'un bug sur le mode dev qui paramétrait les mauvaises valeurs au sein de l'effectif. [#3203](https://github.com/SocialGouv/egapro/issues/3203)
- Mise à jour des dépendances. [#3201](https://github.com/SocialGouv/egapro/issues/3201)
