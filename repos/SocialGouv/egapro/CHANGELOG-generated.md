## Changelog : egapro (30 derniers jours, au 2026-04-30)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface utilisateur, notamment dans les espaces "Mon Espace" et de connexion, en alignement avec les retours Figma. Des fonctionnalités d'administration ont été ajoutées ou améliorées, comme la gestion des référents, la recherche de déclarations et la configuration des campagnes. Des optimisations techniques ont également été apportées, notamment concernant la gestion des fichiers, l'audit et l'intégration de nouvelles technologies comme Valkey pour la mise en cache.

### Évolutions fonctionnelles
- **Mon Espace:** Alignement de l'interface utilisateur avec les maquettes Figma, améliorant l'expérience utilisateur. [#3319](https://github.com/SocialGouv/egapro/issues/3319) [#3344](https://github.com/SocialGouv/egapro/issues/3344)
- **Page de connexion:** Rafraîchissement de l'interface utilisateur de la page de connexion, également en accord avec les retours Figma. [#3318](https://github.com/SocialGouv/egapro/issues/3318) [#3340](https://github.com/SocialGouv/egapro/issues/3340)
- **Déclaration:** Amélioration de la formulation et du poids des consignes, en suivant les directives Figma. [#3321](https://github.com/SocialGouv/egapro/issues/3321) [#3330](https://github.com/SocialGouv/egapro/issues/3330)
- **Page d'accueil:** Amélioration de l'en-tête, de la section "hero", des notifications, de la recherche et de la bannière de ressources. [#3317](https://github.com/SocialGouv/egapro/issues/3317) [#3339](https://github.com/SocialGouv/egapro/issues/3339)
- **Administration:** Ajout d'un graphique de progression des campagnes statistiques. [#3286](https://github.com/SocialGouv/egapro/issues/3286)
- **Filtre par taille d'entreprise:** Ajout d'un filtre par taille d'entreprise avec les plages définies. [#3283](https://github.com/SocialGouv/egapro/issues/3283)
- **Administration:** Ajout d'un lien vers les déclarations dans le menu latéral de l'administration. [#3275](https://github.com/SocialGouv/egapro/issues/3275)
- **Mimoquage (impersonation):** Possibilité d'impersonner une entreprise en mode lecture seule. [#3188](https://github.com/SocialGouv/egapro/issues/3188)
- **Administration:** Gestion des variables globales de campagne. [#3229](https://github.com/SocialGouv/egapro/issues/3229)
- **Administration:** Gestion des référents (CRUD, import/export, API publique). [#3198](https://github.com/SocialGouv/egapro/issues/3198)
- **Recherche multi-critères:** Ajout d'une recherche multi-critères pour les déclarations en administration. [#3196](https://github.com/SocialGouv/egapro/issues/3196)
- **Sitemap et robots.txt:** Ajout d'un sitemap.xml et d'un robots.txt pour le SEO. [#3235](https://github.com/SocialGouv/egapro/issues/3235)
- **Préremplissage:** Préremplissage des données à partir de la dernière déclaration (indicateur 7). [#3246](https://github.com/SocialGouv/egapro/issues/3246) [#3269](https://github.com/SocialGouv/egapro/issues/3269)

### Évolutions techniques
- **API Gateway:** Ajout d'un composant API Gateway. [#3304](https://github.com/SocialGouv/egapro/issues/3304)
- **Valkey:** Intégration de Valkey pour la mise en cache Redis-compatible avec Next.js. [#3228](https://github.com/SocialGouv/egapro/issues/3228)
- **Audit:** Mise en place d'une infrastructure d'audit logging et instrumentation des actions utilisateurs. [#3190](https://github.com/SocialGouv/egapro/issues/3190) [#3192](https://github.com/SocialGouv/egapro/issues/3192) [#3191](https://github.com/SocialGouv/egapro/issues/3191) [#3193](https://github.com/SocialGouv/egapro/issues/3193)
- **Mail:** Configuration de l'envoi d'accusés de réception par email avec Tipimail. [#3237](https://github.com/SocialGouv/egapro/issues/3237) [#3238](https://github.com/SocialGouv/egapro/issues/3238)
- **Schéma:** Script de post-traitement et workflow pour les annotations SUIT/GIP-MDS. [#3341](https://github.com/SocialGouv/egapro/issues/3341)
- **Refactoring:** Suppression des filtres "Index" et "Valeur" dans l'administration des déclarations. [#3276](https://github.com/SocialGouv/egapro/issues/3276)
- **Refactoring:** Suppression du filtre par nom des référents dans l'administration et la recherche publique. [#3281](https://github.com/SocialGouv/egapro/issues/3281) [#3282](https://github.com/SocialGouv/egapro/issues/3282)
- **Optimisation:** Nettoyage de la table "user" en supprimant les colonnes redondantes. [#3122](https://github.com/SocialGouv/egapro/issues/3122)

### Autres changements
- **Documentation:** Ajout de la documentation de référence de l'API SUIT. [#3284](https://github.com/SocialGouv/egapro/issues/3284)
- **Amélioration des tests:** Correction de l'alignement des champs numériques dans la déclaration. [#3255](https://github.com/SocialGouv/egapro/issues/3255) [#3285](https://github.com/SocialGouv/egapro/issues/3285)
- **Automatisation:** Ajout d'un pipeline d'IA. [#3305](https://github.com/SocialGouv/egapro/issues/3305)
- **Workflow:** Automatisation du nettoyage des worktrees et ajout de la commande `/open skill` pour les tests PR locaux. [#3345](https://github.com/SocialGouv/egapro/issues/3345)
- **Correction de bugs:** Diverses corrections de bugs concernant l'affichage, la navigation et la gestion des données.
