## Changelog : egapro (30 derniers jours, au 2026-05-04)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'interface utilisateur, notamment l'alignement avec les maquettes Figma, et l'ajout de nouvelles fonctionnalités pour l'administration et la gestion des données. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Amélioration de l'alignement de l'interface utilisateur des étapes de déclaration avec les maquettes Figma, incluant l'étape des effectifs, le récapitulatif et la modale CSE. [#3320](https://github.com/SocialGouv/egapro/issues/3320), [#3371](https://github.com/SocialGouv/egapro/issues/3371)
- Amélioration de l'alignement de l'interface utilisateur de "Mon Espace" et de la page de connexion avec les maquettes Figma. [#3319](https://github.com/SocialGouv/egapro/issues/3319), [#3344](https://github.com/SocialGouv/egapro/issues/3344), [#3318](https://github.com/SocialGouv/egapro/issues/3340)
- Amélioration de l'alignement du libellé et du poids des consignes avec les maquettes Figma. [#3321](https://github.com/SocialGouv/egapro/issues/3330)
- Amélioration de l'interface utilisateur de l'étape 5 de la déclaration, avec des corrections d'accessibilité et de rendu côté serveur. [#3324](https://github.com/SocialGouv/egapro/issues/3361)
- Ajout d'un graphique de progression de campagne pour l'administration. [#3286](https://github.com/SocialGouv/egapro/issues/3286)
- Ajout d'un filtre de taille d'entreprise. [#3283](https://github.com/SocialGouv/egapro/issues/3283)
- Ajout d'une passerelle API. [#3304](https://github.com/SocialGouv/egapro/issues/3304)
- Ajout de la documentation de référence de l'API SUIT. [#3284](https://github.com/SocialGouv/egapro/issues/3284)
- Amélioration de l'affichage des couleurs et de l'état des choix dans "Mon Espace". [#3207](https://github.com/SocialGouv/egapro/issues/3280)
- Ajout d'un lien vers les déclarations dans le menu latéral de l'administration. [#3275](https://github.com/SocialGouv/egapro/issues/3275)
- Amélioration de la gestion de l'interruption des flux de téléchargement et assainissement des métadonnées d'audit. [#3272](https://github.com/SocialGouv/egapro/issues/3272)
- Ajout de la possibilité de récupérer les catégories d'emplois de l'année précédente (indicateur G). [#3146](https://github.com/SocialGouv/egapro/issues/3146)
- Ajout de la possibilité d'impersonner une entreprise en mode "mimoquage" dans l'administration. [#3188](https://github.com/SocialGouv/egapro/issues/3188)
- Ajout d'un contrôle d'accès administrateur (rôle isAdmin). [#3187](https://github.com/SocialGouv/egapro/issues/3187)
- Ajout d'une carte sitemap et d'un fichier robots.txt pour le SEO. [#3235](https://github.com/SocialGouv/egapro/issues/3235)
- Ajout d'une couche de cache Redis compatible Valkey pour Next.js. [#3228](https://github.com/SocialGouv/egapro/issues/3228)
- Mise en place de MailDev et envoi des accusés de réception par email. [#3177](https://github.com/SocialGouv/egapro/issues/3231)
- Ajout d'une page de recherche publique des référents. [#3186](https://github.com/SocialGouv/egapro/issues/3234)
- Ajout de la configuration des dates limites de campagne via la base de données. [#3140](https://github.com/SocialGouv/egapro/issues/3140)

### Évolutions techniques
- Script de post-traitement et workflow pour les annotations SUIT/GIP-MDS. [#3341](https://github.com/SocialGouv/egapro/issues/3341)
- Automatisation du nettoyage des worktrees et ajout de la commande `/open skill` pour les tests PR locaux. [#3345](https://github.com/SocialGouv/egapro/issues/3345)
- Pipeline d'IA. [#3305](https://github.com/SocialGouv/egapro/issues/3305)
- Suppression des filtres "Index" et "Valeur" sur la page `/admin/declarations`. [#3276](https://github.com/SocialGouv/egapro/issues/3276)
- Suppression du filtre de nom des référents dans l'administration et la recherche publique. [#3281](https://github.com/SocialGouv/egapro/issues/3282)
- Refactorisation de l'audit : Job Cron pour le nettoyage direct de la base de données. [#3270](https://github.com/SocialGouv/egapro/issues/3270)
- Mise en place de Tipimail SMTP en production. [#3237](https://github.com/SocialGouv/egapro/issues/3238)
- Amélioration de la gestion des erreurs et des validations côté serveur.
- Correction de l'alignement des champs numériques. [#3255](https://github.com/SocialGouv/egapro/issues/3285)

### Autres changements
- Documentation de l'API SUIT ajoutée.
- Correction de bugs mineurs d'interface utilisateur et d'accessibilité.
- Mise à jour des dépendances.
- Nettoyage du code.
