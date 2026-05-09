## Changelog : egapro (30 derniers jours, au 07 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment dans le parcours de déclaration, ainsi que par des avancées importantes sur l'infrastructure et l'observabilité de la plateforme. Des efforts ont également été déployés pour renforcer la sécurité et l'administration de l'application.

### Évolutions fonctionnelles
- Amélioration du parcours de déclaration :
    - Pré-remplissage des données à partir de la déclaration précédente avec un indicateur clair. [#3246](https://github.com/SocialGouv/egapro/issues/3246)
    - Alignement de l'interface utilisateur des étapes de déclaration (effectifs, récapitulatif, avis CSE) avec les maquettes Figma. [#3320](https://github.com/SocialGouv/egapro/issues/3320), [#3325](https://github.com/SocialGouv/egapro/issues/3325), [#3324](https://github.com/SocialGouv/egapro/issues/3324)
    - Optimisation de l'étape 5 du formulaire de déclaration (UI, accessibilité, rendu côté serveur). [#3361](https://github.com/SocialGouv/egapro/issues/3361)
    - Fusion des champs "Nom" et "Détail" en un seul champ "Libellé" dans la déclaration. [#3360](https://github.com/SocialGouv/egapro/issues/3360)
- Amélioration de l'espace personnel ("Mon Espace") et de la page de connexion, alignées avec les dernières maquettes Figma. [#3344](https://github.com/SocialGouv/egapro/issues/3344), [#3340](https://github.com/SocialGouv/egapro/issues/3340)
- Ajout d'une page de recherche publique des référents. [#3234](https://github.com/SocialGouv/egapro/issues/3234)
- Implémentation de la gestion des variables globales de campagne dans l'administration. [#3229](https://github.com/SocialGouv/egapro/issues/3229)
- Ajout d'un graphique de progression des campagnes dans l'administration. [#3286](https://github.com/SocialGouv/egapro/issues/3286)
- Ajout d'un filtre par taille d'entreprise dans l'administration. [#3283](https://github.com/SocialGouv/egapro/issues/3283)
- Ajout d'un lien "Déclarations" dans le menu latéral de l'administration. [#3275](https://github.com/SocialGouv/egapro/issues/3275)
- Mise en place d'un système de "mimoquage" (impersonation) d'entreprises dans l'administration. [#3188](https://github.com/SocialGouv/egapro/issues/3188)
- Ajout d'un contrôle d'accès basé sur les rôles dans l'administration (isAdmin). [#3187](https://github.com/SocialGouv/egapro/issues/3187)
- Ajout d'un sitemap.xml et d'un robots.txt pour le SEO. [#3235](https://github.com/SocialGouv/egapro/issues/3235)
- Blocage de la modification des déclarations après la date limite de la campagne. [#3162](https://github.com/SocialGouv/egapro/issues/3162)

### Évolutions techniques
- Mise en place d'une infrastructure d'audit logging pour suivre les actions des utilisateurs. [#3191](https://github.com/SocialGouv/egapro/issues/3191), [#3193](https://github.com/SocialGouv/egapro/issues/3193)
- Intégration de Tipimail pour l'envoi des accusés de réception par email. [#3237](https://github.com/SocialGouv/egapro/issues/3237), [#3238](https://github.com/SocialGouv/egapro/issues/3238)
- Ajout d'une couche de cache Redis avec Valkey pour améliorer les performances de Next.js. [#3228](https://github.com/SocialGouv/egapro/issues/3228)
- Mise en place d'un proxy sécurisé pour le téléchargement de fichiers S3. [#3171](https://github.com/SocialGouv/egapro/issues/3171)
- Refactoring de la recherche des référents pour supprimer les filtres inutiles. [#3281](https://github.com/SocialGouv/egapro/issues/3281), [#3282](https://github.com/SocialGouv/egapro/issues/3282), [#3276](https://github.com/SocialGouv/egapro/issues/3276)
- Amélioration de la pipeline CI/CD pour l'observabilité (événements de phase, coût en direct, détection de blocages). [#3410](https://github.com/SocialGouv/egapro/issues/3410)
- Ajout d'un gateway API. [#3304](https://github.com/SocialGouv/egapro/issues/3304)

### Autres changements
- Documentation de l'API SUIT. [#3284](https://github.com/SocialGouv/egapro/issues/3284)
- Mise à jour des dépendances.
- Nettoyage du code et corrections de bugs mineurs.
- Amélioration de la gestion des erreurs et des messages d'information.
- Ajout de constantes et d'helpers pour les quartiles. [#3359](https://github.com/SocialGouv/egapro/issues/3359)
- Mise en place d'un script de post-processing pour les annotations SUIT/GIP-MDS. [#3341](https://github.com/SocialGouv/egapro/issues/3341)
- Amélioration de la pipeline pour l'intégration des épics et l'enrichissement des tickets. [#3367](https://github.com/SocialGouv/egapro/issues/3367)
- Correction de bugs d'orchestration de la pipeline épique. [#3403](https://github.com/SocialGouv/egapro/issues/3403)
- Correction d'un bug lié à la variable d'environnement CLAUDECODE. [#3407](https://github.com/SocialGouv/egapro/issues/3407)
