## Changelog : monstagedeseconde (30 derniers jours)

### Résumé
Les dernières mises à jour de MonStageDeSeconde améliorent la gestion des conventions de stage, notamment pour les établissements scolaires et les entreprises. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant la recherche d'offres de stage et la signature électronique. Des améliorations techniques ont également été réalisées pour optimiser le code et l'infrastructure.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la fonction "offre inadaptée" de fonctionner correctement (#770).
- Amélioration du script de doublonnage d'offres pour ignorer les offres défectueuses qui ne peuvent pas être sauvegardées (#772).
- Amélioration de l'envoi d'emails pour les signatures de conventions (#771).
- Amélioration de la gestion des places disponibles pour les offres de stage collège et lycée (#756).
- Amélioration de l'interface d'administration des établissements scolaires (#754).
- Correction d'un bug dans la recherche d'offres de stage pour les étudiants.
- Amélioration de la gestion des conventions mono et multi-établissements avec l'ajout de cases à cocher (#749, #753).
- Ajout d'une nouvelle gem `letter_thief` pour améliorer les fonctionnalités liées aux lettres (#750).
- Amélioration de la vue pour la gestion des accords multiples, permettant aux gestionnaires d'école de signer (#752).

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `rack` (3.2.4 -> 3.2.5), `qs` (6.14.1 -> 6.14.2), `faraday` (2.14.0 -> 2.14.1), `diff` (5.2.0 -> 5.2.2), `copier` (9.9.1 -> 9.11.2), `lodash` (4.17.21 -> 4.17.23).
- Refactorisation du code pour retirer des assignations vides (#763).
- Configuration du Ruby LSP.
- Amélioration des tests KPI et correction de bugs associés.
- Suppression de paramètres de production inutiles dans `structure.sql`.
- Ajout de la déclaration `openssh` dans le `Gemfile`.
- Correction de bugs et amélioration des tests liés à la reconstruction des revues.
- Suppression de `InternshipOfferInfo`.

### Autres changements
- Mise à jour de la documentation et correction de fautes de frappe.
- Amélioration du versionnement des fichiers de configuration.
- Synchronisation des scripts de configuration.
- Correction de problèmes de typographie et d'accents.
- Suppression de code obsolète.
- Correction de problèmes liés à l'affichage des images PNG.
- Correction de bugs dans les tests CI.
