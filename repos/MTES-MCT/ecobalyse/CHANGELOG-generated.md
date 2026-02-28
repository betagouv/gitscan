## Changelog : ecobalyse (30 derniers jours)

### Résumé
Les dernières mises à jour d'ecobalyse apportent des améliorations à l'interface utilisateur, notamment concernant les fenêtres modales et les champs de recherche, ainsi que des corrections de bugs pour une meilleure stabilité. De nouvelles fonctionnalités ont été ajoutées, comme l'exportation et l'importation de favoris, et l'affichage des impacts des textiles. Des optimisations techniques ont également été réalisées pour améliorer la sécurité et la performance.

### Évolutions fonctionnelles
- Possibilité d'exporter et d'importer les favoris (#1784)
- Affichage des impacts des textiles dans les réponses de l'API (#1835)
- Ajout d'une bannière d'avertissement lorsque les conditions d'utilisation ne sont pas acceptées (#1817)
- Expression de la masse des vêtements textiles en grammes (#1818)
- Amélioration des icônes des favoris (#1823)
- Correction d'un bug empêchant la fermeture des fenêtres modales en cliquant en dehors (#1825)
- Correction d'un bug d'autofocus sur le champ de recherche dans certaines fenêtres modales (#1824)
- Correction d'un message de bannière erroné (#1822)
- Correction d'un problème d'authentification dans l'historique des scores (#1845)
- Correction d'un bug lié à l'export après encodage (#1857)
- Correction d'un bug lié à la nouvelle base de données Ginko pour l'export (#1820)

### Évolutions techniques
- Authentification requise pour toutes les appels à l'API (#1779)
- Suppression du code de version obsolète (#1792)
- Mise à jour des dépendances NodeJS (#1842)
- Amélioration de l'implémentation de l'autofocus pour l'autocomplétion (#1834)
- Suppression des actions de création de release (#1783)
- Amélioration de la gestion du chargement des processus en production (#1786)
- Correction d'un problème lié à la variable non liée (#1855)
- Autorisation de toutes les valeurs pour le paramètre `sslmode` dans la chaîne de connexion PostgreSQL (#1852)
- Suppression des logs d'erreurs d'authentification vers Sentry (#1858)
- Passage à Litestar 2.20.0 (#1780)

### Autres changements
- Ajout de nouveaux ingrédients dans les données (#1670)
- Tri des processus (#1843)
- Mise à jour des composants (#1776)
- Mise à jour des dépendances npm (#1775)
