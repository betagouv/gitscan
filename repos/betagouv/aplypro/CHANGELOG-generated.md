## Changelog : aplypro (30 derniers jours)

### Résumé
Les récentes mises à jour d'APLyPro se concentrent sur l'amélioration de la gestion des paiements, notamment en activant les paiements MER et en corrigeant des problèmes liés aux rectifications. Des améliorations techniques ont également été apportées pour assurer la stabilité et la conformité du code.

### Évolutions fonctionnelles
- Activation des paiements MER (Mouvement Économique Régional) (#1890, #1892).
- Blocage des demandes de paiement ENPR (Établissement National de Perfectionnement Régional) (#1886).
- Gestion améliorée des rectifications :
    - Journalisation des échecs de lecture des rectifications (#1901).
    - Les rectifications négatives sont maintenant conservées dans l'état "en attente".
    - Correction du format de la date PFMP stockée avec `codeobjet` (#1896).

### Évolutions techniques
- Mise à jour de plusieurs dépendances :
    - `nokogiri` de 1.19.0 à 1.19.1 (#1898).
    - `rack` de 3.2.4 à 3.2.5 (#1897).
    - `faraday` de 2.14.0 à 2.14.1 (#1893).
- Refactoring : remplacement du `codeobjet` par `codecheance` (#1892).
- Amélioration de la qualité du code avec des corrections Rubocop (#1889, #1890).
- Ajout de tests unitaires pour `paid_amount` et le format `codeobjet` (#1896).
- Mise à jour de la version de l'application à 2.8.7 (#1892).

### Autres changements
- Mise à jour du fichier `bundle` (#1889, #1890).
