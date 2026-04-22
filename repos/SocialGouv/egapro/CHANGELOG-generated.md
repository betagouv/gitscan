## Changelog : egapro (30 derniers jours, au 2026-04-21)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans l'espace "Mon Espace" et l'administration, ainsi que sur le renforcement de la sécurité et de l'infrastructure. Des améliorations ont été apportées à la gestion des déclarations, à l'export des données et à l'audit des actions utilisateurs. L'implémentation d'un système de cache et l'utilisation de Tipimail pour l'envoi d'emails sont également des nouveautés importantes.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de pré-remplissage des déclarations à partir de la dernière déclaration avec l'indicateur 7. [#3246](https://github.com/SocialGouv/egapro/issues/3246) [#3269](https://github.com/SocialGouv/egapro/issues/3269)
- Amélioration du "mimoquage" (impersonation) : actualisation du numéro de téléphone, suppression de la modale d'informations manquantes et restauration de la bannière. [#3253](https://github.com/SocialGouv/egapro/issues/3253)
- Suivi de la finalisation de l'avis du CSE avec un horodatage dédié. [#3271](https://github.com/SocialGouv/egapro/issues/3271)
- Ajout d'une page de recherche publique des référents. [#3186](https://github.com/SocialGouv/egapro/issues/3234)
- Possibilité d'éditer les variables globales de campagne dans l'administration. [#3229](https://github.com/SocialGouv/egapro/issues/3229)
- Gestion des référents dans l'administration (CRUD, import/export, API publique). [#3198](https://github.com/SocialGouv/egapro/issues/3198)
- Ajout d'une attestation de non-sanction (PDF). [#3089](https://github.com/SocialGouv/egapro/issues/3089)
- Amélioration de la navigation et des champs en lecture seule dans le "mimoquage". [#3252](https://github.com/SocialGouv/egapro/issues/3252)
- Ajout d'un sitemap.xml et d'un robots.txt publics pour le SEO. [#3235](https://github.com/SocialGouv/egapro/issues/3235)
- Ajout d'une fonctionnalité permettant de bloquer l'écriture en mode "mimoquage" pour éviter les modifications accidentelles. [#3232](https://github.com/SocialGouv/egapro/issues/3232)
- Ajout de la possibilité de télécharger des fichiers d'évaluation conjointe et d'avis CSE via l'API. [#2905](https://github.com/SocialGouv/egapro/issues/3200)
- Amélioration de l'affichage du nombre total de salariés dans l'étape 5 de la déclaration. [#3160](https://github.com/SocialGouv/egapro/issues/3163)
- Ajout d'une fonctionnalité de recherche multi-critères des déclarations dans l'administration. [#3196](https://github.com/SocialGouv/egapro/issues/3196)
- Ajout d'une barre latérale de navigation dans l'interface d'administration. [#3195](https://github.com/SocialGouv/egapro/issues/3195)
- Ajout de la possibilité de configurer les dates limites de campagne via la base de données. [#3140](https://github.com/SocialGouv/egapro/issues/3140)
- Refonte de la table des déclarations et ajout d'un panneau latéral pour les documents dans "Mon Espace". [#3170](https://github.com/SocialGouv/egapro/issues/3170)
- Mise à jour de la bannière d'informations sur l'entreprise pour correspondre au nouveau design. [#3168](https://github.com/SocialGouv/egapro/issues/3168)
- Ajout d'une bannière de ressources globale sur toutes les pages. [#3075](https://github.com/SocialGouv/egapro/issues/3075)
- Ajout de boutons de téléchargement PDF sur la page de confirmation de la conformité et pour les cartes CSE. [#3057](https://github.com/SocialGouv/egapro/issues/3057), [#3058](https://github.com/SocialGouv/egapro/issues/3058)
- Support de la deuxième variante de déclaration dans la génération de PDF. [#3053](https://github.com/SocialGouv/egapro/issues/3053)

### Évolutions techniques
- Implémentation d'un système de cache Valkey Redis-compatible pour Next.js. [#3228](https://github.com/SocialGouv/egapro/issues/3228)
- Mise en place de Tipimail SMTP en production pour l'envoi d'emails. [#3237](https://github.com/SocialGouv/egapro/issues/3238)
- Mise en place d'une infrastructure d'audit logging et instrumentation des actions utilisateurs. [#3190](https://github.com/SocialGouv/egapro/issues/3192) [#3191](https://github.com/SocialGouv/egapro/issues/3193)
- Sécurisation de la route de téléchargement des fichiers S3 avec un proxy. [#3171](https://github.com/SocialGouv/egapro/issues/3171)
- Migration de l'authentification de sessions de base de données vers JWT. [#3030](https://github.com/SocialGouv/egapro/issues/3030)
- Automatisation de la modification du wiki lors de l'évolution du schéma de la base de données. [#3147](https://github.com/SocialGouv/egapro/issues/3147)
- Ajout d'un certificat pour l'API privée SUIT. [#3120](https://github.com/SocialGouv/egapro/issues/3120)
- Refactor de la table `user` pour supprimer les colonnes redondantes. [#3122](https://github.com/SocialGouv/egapro/issues/3122)
- Refactor de la table `declaration_category` pour typer les colonnes d'indicateurs. [#3106](https://github.com/SocialGouv/egapro/issues/3106)
- Mise en place d'un lifecycle basé sur 4 skills pour la gestion du code. [#3108](https://github.com/SocialGouv/egapro/issues/3108)
- Nettoyage et refactoring du code pour améliorer la maintenabilité.
- Mise à jour des dépendances. [#3201](https://github.com/SocialGouv/egapro/issues/3201)

### Autres changements
- Ajout d'une documentation OpenAPI 3.1 et d'une interface Swagger UI pour l'API d'export des déclarations. [#3042](https://github.com/SocialGouv/egapro/issues/3042)
- Correction d'un bug sur le mode développement qui paramétrait de mauvaises valeurs au sein de l'effectif. [#3203](https://github.com/SocialGouv/egapro/issues/3203)
- Correction d'un bug lié à l'affichage du bouton de déconnexion et des informations utilisateur sur mobile. [#3173](https://github.com/SocialGouv/egapro/issues/3173)
- Correction de divers problèmes d'interface utilisateur et d'accessibilité.
- Mise en place de MailDev et envoi des accusés de réception. [#3177](https://github.com/SocialGouv/egapro/issues/3231)
- Correction de l'utilisation de l'identifiant ProConnect dans le JWT. [#3099](https://github.com/SocialGouv/egapro/issues/3099)
- Suppression du cookie de session sécurisé avec les attributs correspondants lors de la déconnexion. [#3098](https://github.com/SocialGouv/egapro/issues/3098)
- Correction de l'importation des données GIP MDS. [#3035](https://github.com/SocialGouv/egapro/issues/3035) [#3031](https://github.com/SocialGouv/egapro/issues/3031)
- Correction de l'erreur de migration sur la table gip mds. [#3028](https://github.com/SocialGouv/egapro/issues/3028)
- Correction de l'affichage des séparateurs de milliers dans les champs de salaire de l'indicateur G. [#3094](https://github.com/SocialGouv/egapro/issues/3094)
- Correction de l'ordre des options de parcours de conformité et des bordures. [#3054](https://github.com/SocialGouv/egapro/issues/3054)
- Correction de l'affichage des titres sur les pages d'erreur. [#3078](https://github.com/SocialGouv/egapro/issues/3078)
- Correction de l'affichage des bordures des cartes d'opinion CSE. [#3056](https://github.com/SocialGouv/egapro/issues/3056)
- Correction de l'affichage des barres de progression. [#2687](https://github.com/SocialGouv/egapro/issues/2687)
- Correction de l'étiquetage des champs de formulaire pour l'accessibilité. [#2682](https://github.com/SocialGouv/egapro/issues/2682)
- Mise à jour de la description du pied de page. [#2934](https://github.com/SocialGouv/egapro/issues/3084)
- Refonte de la page "Mon Espace" selon les maquettes Figma. [#2936](https://github.com/SocialGouv/egapro/issues/3076)
