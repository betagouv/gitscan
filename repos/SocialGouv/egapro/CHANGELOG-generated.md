## Changelog : egapro (30 derniers jours, au 2026-04-28)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans l'espace "Mon Espace" et l'administration, avec de nouvelles fonctionnalités de recherche, de navigation et de gestion des données. Des améliorations techniques significatives ont également été apportées, notamment en matière d'audit, de sécurité et de performance.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de nettoyage automatique des worktrees pour faciliter les tests en local ([#3345](https://github.com/SocialGouv/egapro/issues/3345)).
- Amélioration de l'alignement des champs numériques dans la déclaration. ([#3255](https://github.com/SocialGouv/egapro/issues/3255) et [#3285](https://github.com/SocialGouv/egapro/issues/3285)).
- Ajout d'un graphique de progression de la campagne dans l'espace administrateur ([#3286](https://github.com/SocialGouv/egapro/issues/3286)).
- Ajout d'un filtre de taille d'entreprise ([#3283](https://github.com/SocialGouv/egapro/issues/3283)).
- Amélioration de l'expérience utilisateur dans "Mon Espace" avec la mise à jour des couleurs du panneau latéral et la gestion de l'état du deuxième tour ([#3207](https://github.com/SocialGouv/egapro/issues/3207) et [#3280](https://github.com/SocialGouv/egapro/issues/3280)).
- Suppression des filtres "Index" et "Valeur" dans l'interface d'administration des déclarations ([#3276](https://github.com/SocialGouv/egapro/issues/3276)).
- Ajout d'un lien vers les déclarations dans le menu latéral de l'administration ([#3275](https://github.com/SocialGouv/egapro/issues/3275)).
- Amélioration de la gestion des téléchargements avec l'annulation des flux sur déconnexion du client et la sanitisation des métadonnées d'audit ([#3272](https://github.com/SocialGouv/egapro/issues/3272)).
- Amélioration de la déduction automatique de l'année active et de la date GIP dans l'administration ([#3279](https://github.com/SocialGouv/egapro/issues/3279)).
- Ajout d'une exigence de filtre avant la recherche de référents et amélioration de la robustesse de la recherche ([#3278](https://github.com/SocialGouv/egapro/issues/3278)).
- Masquage du pied de page public et de la bannière d'aide sur les routes d'administration ([#3277](https://github.com/SocialGouv/egapro/issues/3277)).
- Pré-remplissage des données de la déclaration précédente avec un indicateur spécifique ([#3246](https://github.com/SocialGouv/egapro/issues/3246) et [#3269](https://github.com/SocialGouv/egapro/issues/3269)).
- Amélioration de l'interface de "mimoquage" avec des champs en lecture seule, la navigation entre les étapes enregistrées et la restauration de la bannière ([#3253](https://github.com/SocialGouv/egapro/issues/3253)).
- Suivi de la finalisation de l'avis du CSE avec un horodatage dédié ([#3271](https://github.com/SocialGouv/egapro/issues/3271)).
- Ajout d'un sitemap et d'un fichier robots.txt pour le SEO ([#3235](https://github.com/SocialGouv/egapro/issues/3235)).
- Amélioration de l'interface de "mimoquage" avec des champs en lecture seule et la navigation entre les étapes ([#3252](https://github.com/SocialGouv/egapro/issues/3252)).
- Amélioration de la fenêtre de signature SUIT en fonction de l'environnement ([#3250](https://github.com/SocialGouv/egapro/issues/3250)).
- Ajout de la gestion de l'impersonation d'une entreprise dans l'administration ([#3188](https://github.com/SocialGouv/egapro/issues/3188)).
- Ajout d'un contrôle d'accès administrateur à l'interface d'administration ([#3187](https://github.com/SocialGouv/egapro/issues/3187)).
- Ajout d'un panneau latéral avec l'état de conformité de la déclaration ([#3107](https://github.com/SocialGouv/egapro/issues/3107)).

### Évolutions techniques
- Mise en place d'une infrastructure d'audit logging ([#3190](https://github.com/SocialGouv/egapro/issues/3190) et [#3192](https://github.com/SocialGouv/egapro/issues/3192)) et instrumentation des actions utilisateurs ([#3191](https://github.com/SocialGouv/egapro/issues/3191) et [#3193](https://github.com/SocialGouv/egapro/issues/3193)).
- Ajout d'une couche de cache Valkey Redis-compatible pour Next.js ([#3228](https://github.com/SocialGouv/egapro/issues/3228)).
- Mise en place de MailDev et envoi des accusés de réception par email ([#3177](https://github.com/SocialGouv/egapro/issues/3177) et [#3231](https://github.com/SocialGouv/egapro/issues/3231)).
- Ajout d'un proxy sécurisé pour le téléchargement de fichiers S3 ([#3171](https://github.com/SocialGouv/egapro/issues/3171)).
- Refactor de la table `user` pour supprimer les colonnes redondantes ([#3122](https://github.com/SocialGouv/egapro/issues/3122)).
- Lier les données GIP MDS à la société par clé étrangère siren et importer quotidiennement ([#3110](https://github.com/SocialGouv/egapro/issues/3110)).
- Aplatir la catégorie de déclaration en colonnes d'indicateurs typées ([#3106](https://github.com/SocialGouv/egapro/issues/3106)).
- Lier CSE et évaluation conjointe à la déclaration ([#3111](https://github.com/SocialGouv/egapro/issues/3111)).
- Ajout d'un certificat pour l'API privée SUIT ([#3120](https://github.com/SocialGouv/egapro/issues/3120)).
- Mise en place d'un lifecycle basé sur 4 skills pour la gestion du code : analyse, implémentation, revue et déploiement ([#3108](https://github.com/SocialGouv/egapro/issues/3108)).
- Ajout d'un mécanisme de vérification de la clé API SUIT et sécurisation de l'endpoint d'export des déclarations ([#3082](https://github.com/SocialGouv/egapro/issues/3082)).

### Autres changements
- Ajout de documentation de référence pour l'API ([#3284](https://github.com/SocialGouv/egapro/issues/3284)).
- Ajout d'une API pour les fichiers d'avis du CSE et d'évaluation conjointe ([#3085](https://github.com/SocialGouv/egapro/issues/3085)).
- Automatisation de la modification du wiki lorsque le schéma de la base de données évolue ([#3147](https://github.com/SocialGouv/egapro/issues/3147)).
- Correction d'un bug sur le mode dev qui paramétrait les mauvaises valeurs au sein de l'effectif ([#3203](https://github.com/SocialGouv/egapro/issues/3203)).
- Mise à jour des dépendances et suppression de `baseUrl` redondant ([#3201](https://github.com/SocialGouv/egapro/issues/3201)).
- Stockage de l'identifiant ProConnect dans le JWT ([#3099](https://github.com/SocialGouv/egapro/issues/3099)).
- Suppression de la session cookie sécurisée avec les attributs correspondants ([#3098](https://github.com/SocialGouv/egapro/issues/3098)).
