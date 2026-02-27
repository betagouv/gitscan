## Changelog : monstagedeseconde (30 derniers jours)

### Résumé
Les dernières mises à jour de MonStageDeSeconde améliorent la gestion des conventions de stage, notamment pour les établissements scolaires et les entreprises. Des corrections de bugs ont été apportées pour améliorer la fiabilité de la plateforme, ainsi que des optimisations pour l'import de données et la recherche d'offres. L'interface a également été améliorée, notamment au niveau de la recherche et de la gestion des établissements scolaires.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la fonction "offres inappropriées" de fonctionner correctement (#770).
- Amélioration du script d'import d'offres pour ignorer les offres défectueuses qui ne peuvent pas être sauvegardées (#772).
- Amélioration de la gestion des signatures pour les responsables d'établissement scolaire (#752).
- Ajout de la possibilité de filtrer les offres de stage par secteur (#754).
- Correction de l'affichage des conventions mono et multi-établissements (#749, #753).
- Amélioration de la recherche d'offres de stage (#748, #754).
- Correction de l'affichage des établissements scolaires dans l'interface d'administration (#750).
- Correction de bugs liés à la recherche d'offres pour les étudiants (#746).
- Amélioration de la gestion des places disponibles pour les offres de stage (#756).
- Ajout d'une contrainte de base de données pour le secteur (#753).

### Évolutions techniques
- Mise à jour de la configuration Ruby LSP.
- Refactorisation du code pour supprimer des assignations vides (#763).
- Amélioration de la gestion des emails envoyés pour les signatures de conventions (#771).
- Mise à jour des tests KPI (#769).
- Mise à jour des dépendances : Rack (3.2.4 -> 3.2.5), qs (6.14.1 -> 6.14.2), faraday (2.14.0 -> 2.14.1), diff (5.2.0 -> 5.2.2), copier (9.9.1 -> 9.11.2) (#767, #769, #746, #747).
- Utilisation de `update` au lieu de `create` pour compter les nouveaux étudiants dans les emails KPI.
- Suppression de paramètres de production inutiles dans le fichier `structure.sql`.
- Ajout de la déclaration d'OpenSSH dans le Gemfile.
- Suppression de `InternshipOfferInfo`.

### Autres changements
- Correction de fautes d'orthographe et d'accents (#750).
- Amélioration de la gestion des fichiers de configuration et synchronisation des scripts (#749).
- Correction de bugs dans les tests (#769, #751).
- Suppression de fichiers de configuration traditionnels et ajout de fichiers cachés pour la gestion des versions.
- Suppression de code obsolète.
- Correction de problèmes liés à l'affichage des images PNG (#753).
- Ajout de tests pour les paramètres optionnels de recherche (#746).
- Précision du wording dans l'interface.
