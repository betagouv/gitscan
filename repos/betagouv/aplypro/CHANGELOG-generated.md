## Changelog : aplypro (30 derniers jours)

### Résumé
Les dernières mises à jour d'APLyPro se concentrent sur l'amélioration de la gestion des paiements, notamment en intégrant les paiements MER et en ajustant le traitement des rectifications. Des corrections de bugs et des améliorations techniques ont également été apportées pour assurer la stabilité et la conformité du code.

### Évolutions fonctionnelles
- Intégration des paiements MER (Ministère de l'Éducation Nationale et de la Recherche) (#1890).
- Blocage des demandes de paiement ENPR (Établissement Pour Non Reconnu) (#1886).
- Amélioration du traitement des rectifications : les rectifications négatives sont maintenant conservées en état "en attente".
- Utilisation du `codeobjet` pour stocker la date PFMP (Plan de Formation en Milieu Professionnel).

### Évolutions techniques
- Mise à jour de plusieurs dépendances :
    - `nokogiri` de 1.19.0 à 1.19.1 (#1898)
    - `rack` de 3.2.4 à 3.2.5 (#1897)
    - `faraday` de 2.14.0 à 2.14.1 (#1893)
- Refactoring pour utiliser `codecheance` au lieu de `codeobjet` pour le marquage (#1892).
- Ajout de tests unitaires pour `paid_amount` et le format `codeobjet`.
- Corrections de style avec Rubocop.
- Mise à jour du bundle.
- Log des erreurs de lecture de rectification (#1901).
- Bump de version à 2.8.7 (#1893).

### Autres changements
- Documentation mise à jour (non spécifié dans les commits).
