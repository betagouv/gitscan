## Changelog : egapro (30 derniers jours, au 2026-04-30)

### Résumé
Les dernières semaines ont été marquées par une amélioration significative de l'interface utilisateur, notamment sur les pages "Mon Espace", de connexion et de déclaration, en alignement avec les retours Figma. Des fonctionnalités d'administration ont été ajoutées pour la gestion des référents et des déclarations, ainsi que pour la configuration des campagnes. Des optimisations techniques ont été apportées pour améliorer la performance et la sécurité, notamment avec l'ajout d'un cache Redis et la mise en place d'un système d'audit.

### Évolutions fonctionnelles
- **Mon Espace:** Amélioration de l'alignement de l'interface utilisateur avec les maquettes Figma, incluant l'apparence des étapes et des couleurs. [#3319](https://github.com/SocialGouv/egapro/issues/3319) [#3344](https://github.com/SocialGouv/egapro/issues/3344)
- **Connexion:** Rafraîchissement de la page de connexion pour correspondre aux retours Figma. [#3318](https://github.com/SocialGouv/egapro/issues/3318) [#3340](https://github.com/SocialGouv/egapro/issues/3340)
- **Déclaration:** Alignement du libellé et du poids de la consigne sur la page de déclaration avec les spécifications Figma. [#3321](https://github.com/SocialGouv/egapro/issues/3321) [#3330](https://github.com/SocialGouv/egapro/issues/3330)
- **Page d'accueil:** Amélioration de l'apparence de l'en-tête, de la section principale, des notifications, de la barre de recherche et des bannières de ressources. [#3317](https://github.com/SocialGouv/egapro/issues/3317) [#3339](https://github.com/SocialGouv/egapro/issues/3339)
- **Administration:** Ajout d'un graphique de progression des campagnes dans l'espace administrateur. [#3286](https://github.com/SocialGouv/egapro/issues/3286)
- **Filtres:** Ajout d'un filtre par taille d'entreprise. [#3283](https://github.com/SocialGouv/egapro/issues/3283)
- **Administration:** Ajout d'un lien vers les déclarations dans le menu latéral de l'espace administrateur. [#3275](https://github.com/SocialGouv/egapro/issues/3275)
- **Mimoquage (impersonation):** Possibilité d'impersonner une entreprise en mode lecture seule. [#3188](https://github.com/SocialGouv/egapro/issues/3188)
- **Administration:** Gestion des référents (CRUD, import/export, API publique). [#3198](https://github.com/SocialGouv/egapro/issues/3198)
- **Recherche multi-critères:** Ajout d'une recherche multi-critères des déclarations dans l'espace administrateur. [#3196](https://github.com/SocialGouv/egapro/issues/3196)
- **Campagnes:** Configuration des dates limites des campagnes via la base de données. [#3140](https://github.com/SocialGouv/egapro/issues/3140)
- **Indicateur G:** Récupération des catégories d'emplois de l'année précédente pour l'indicateur G. [#3146](https://github.com/SocialGouv/egapro/issues/3146)
- **Préremplissage:** Préremplissage de la déclaration à partir de la dernière déclaration avec l'indicateur 7. [#3246](https://github.com/SocialGouv/egapro/issues/3246) [#3269](https://github.com/SocialGouv/egapro/issues/3269)

### Évolutions techniques
- **API Gateway:** Ajout d'un composant API Gateway. [#3304](https://github.com/SocialGouv/egapro/issues/3304)
- **Cache:** Implémentation d'une couche de cache Valkey Redis-compatible pour Next.js. [#3228](https://github.com/SocialGouv/egapro/issues/3228)
- **Audit:** Mise en place d'une infrastructure d'audit logging et instrumentation des actions utilisateurs. [#3190](https://github.com/SocialGouv/egapro/issues/3190) [#3192](https://github.com/SocialGouv/egapro/issues/3192) [#3191](https://github.com/SocialGouv/egapro/issues/3191) [#3193](https://github.com/SocialGouv/egapro/issues/3193)
- **Mail:** Configuration de l'envoi des accusés de réception par email avec Tipimail. [#3237](https://github.com/SocialGouv/egapro/issues/3237) [#3238](https://github.com/SocialGouv/egapro/issues/3238)
- **Sitemap & Robots.txt:** Ajout d'un sitemap.xml et d'un robots.txt pour le SEO. [#3235](https://github.com/SocialGouv/egapro/issues/3235)
- **Base de données:** Optimisation de la structure de la base de données (suppression de colonnes redondantes, ajout de clés étrangères). [#3122](https://github.com/SocialGouv/egapro/issues/3122) [#3121](https://github.com/SocialGouv/egapro/issues/3121)
- **SUIT/GIP-MDS:** Script de post-processing et workflow pour les annotations SUIT/GIP-MDS. [#3341](https://github.com/SocialGouv/egapro/issues/3341)
- **Automatisation:** Automatisation de la modification du wiki lorsque le schéma de la base de données évolue. [#3147](https://github.com/SocialGouv/egapro/issues/3147)

### Autres changements
- **Documentation:** Ajout de la documentation de référence de l'API SUIT. [#3284](https://github.com/SocialGouv/egapro/issues/3284)
- **Tests:** Amélioration des tests et correction de bugs.
- **Refactoring:** Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- **Corrections:** Diverses corrections de bugs et améliorations de l'interface utilisateur.
