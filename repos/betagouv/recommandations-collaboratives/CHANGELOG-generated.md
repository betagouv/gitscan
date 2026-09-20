## Changelog : recommandations-collaboratives (30 derniers jours, au 18 septembre 2026)

### Résumé
Ce mois-ci, l'effort de développement a été massivement concentré sur la sécurisation de la plateforme. Des mesures importantes ont été prises pour garantir l'étanchéité des données entre les différentes organisations (prévention des fuites de données) et pour renforcer la protection contre les injections de code. Parallèlement, l'interface d'administration a été enrichie de nouveaux outils de filtrage et la gestion des notifications a été stabilisée.

### Évolutions fonctionnelles
- **Administration** : Ajout de filtres pour identifier les utilisateurs supprimés et les organisations "mystérieuses" dans l'interface de gestion [#2343](https://github.com/betagouv/recommandations-collaboratives/issues/2343).
- **Gestion des utilisateurs** : Amélioration de la validation des adresses e-mail lors de la création ou de la modification de comptes [#2256](https://github.com/betagouv/recommandations-collaboratives/issues/2256).
- **Flux de données** : Les flux RSS filtrent désormais les ressources en mode "brouillon" pour éviter toute diffusion accidentelle de contenus non finalisés.
- **Expérience utilisateur** : Amélioration de la clarté de l'interface via des textes d'aide plus explicites et une meilleure présentation des titres.
- **Corrections** : Résolution d'un problème de doublons dans les notifications de modération [#2335](https://github.com/betagouv/recommandations-collaboratives/issues/2335) et correction du processus d'inscription multi-sites [#2334](https://github.com/betagouv/recommandations-collaboratives/issues/2334).

### Évolutions techniques
- **Sécurité (Renforcement majeur)** :
    - Correction de plusieurs failles de type IDOR permettant d'empêcher l'accès non autorisé aux ressources, projets et documents appartenant à d'autres organisations (cross-tenant) [#2376](https://github.com/betagouv/recommandations-collaboratives/issues/2376), [#2377](https://github.com/betagouv/recommandations-collaboratives/issues/2377), [#2380](https://github.com/betagouv/recommandations-collaboratives/issues/2380).
    - Mise en œuvre et affinement d'une politique de sécurité de contenu (CSP) stricte pour protéger l'application contre les attaques de type XSS [#2342](https://github.com/betagouv/recommandations-collaboratives/issues/2342), [#2330](https://github.com/betagouv/recommandations-collaboratives/issues/2330).
    - Renforcement de la désinfection (sanitization) du contenu HTML et Markdown ainsi que des paramètres d'envoi d'emails pour prévenir les injections [#2374](https://github.com/betagouv/recommandations-collaboratives/issues/2374), [#2381](https://github.com/betagouv/recommandations-collaboratives/issues/2381).
    - Sécurisation du stockage des fichiers privés (enquêtes et documents) par la randomisation de leurs chemins d'accès [#2383](https://github.com/betagouv/recommandations-collaboratives/issues/2383).
    - Protection contre les vulnérabilités de "mass assignment" sur les API de projets [#2382](https://github.com/betagouv/recommandations-collaboratives/issues/2382).
- **CI/CD & Tests** :
    - Intégration d'un audit de sécurité automatique des dépendances frontend (`yarn audit`) dans le pipeline de CI [#2420](https://github.com/betagouv/recommandations-collaboratives/issues/2420).
    - Séparation des tests frontend et backend dans les processus de vérification automatisés.
    - Augmentation significative de la couverture de tests de régression, particulièrement sur les aspects de sécurité et d'accès multi-sites.
- **Architecture & Refactoring** :
    - Refactorisation du mécanisme de chargement des modules et des applications [#2393](https://github.com/betagouv/recommandations-collaboratives/issues/2393).
    - Migration de certains composants vers la version 3.

### Autres changements
- **Documentation** : Amélioration de la documentation relative aux migrations de fichiers et meilleure visibilité des erreurs lors de ces opérations.
- **Maintenance** : Nettoyage général du code (linting) et suppression de méthodes redondantes.
