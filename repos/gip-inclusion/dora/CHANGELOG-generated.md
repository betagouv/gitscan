## Changelog : dora (30 derniers jours, au 18 novembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur un renforcement majeur de la sécurité et de la protection des données (anonymisation, sécurisation des accès et des endpoints). L'expérience utilisateur a également été affinée, notamment via l'amélioration des outils de recherche et la fiabilisation des formulaires et de la gestion des membres.

### Évolutions fonctionnelles
- **Amélioration de la recherche** : partage du dernier lieu sélectionné entre la recherche thématique et la recherche par mots-clés [#1476] et remplacement de la recherche Google par la recherche interne Dora [#1464].
- **Expérience utilisateur** : affichage des coordonnées de la structure si le service n'en possède pas [#1540], nouvelle notice pour le chargement des documents [#1482] et meilleure synchronisation des données lors du rendu des formulaires [#1455].
- **Gestion des accès et adhésions** : redirection des demandes d'orientation vers la plateforme de l'inclusion [#1463], redirection optimisée des administrateurs vers les demandes d'adhésion [#1506] et empêchement de la création de membres en double lors de l'acceptation d'une demande [#1509].
- **Corrections diverses** : masquage du bouton de sauvegarde de recherche pour les utilisateurs déconnectés [#1511] et prévention de l'enregistrement d'utilisateurs sans nom (via ProConnect ou import CSV) [#1471].

### Évolutions techniques
- **Sécurité et protection des données** :
    - Renforcement de l'anonymisation (utilisation d'UUID pour les bénéficiaires et durée d'anonymisation par défaut à 183 jours) [#1551, #1548].
    - Durcissement de la sécurité web via la mise en place d'une politique de sécurité de contenu (CSP) et de nouveaux en-têtes de sécurité [#1530].
    - Suppression d'endpoints de diagnostic et d'upload non authentifiés ou non contrôlés [#1480, #1477, #1478].
    - Limitation et journalisation des tentatives de connexion à l'administration [#1534] et uniformisation des demandes de liens de connexion [#1479].
- **Infrastructure et CI/CD** :
    - Automatisation de la relecture des Pull Requests [#1497] et exigence de passage des tests (back et front) sur chaque PR [#1533].
    - Ajout de contrôles de qualité pour l'analytics (linting SQL, dbt, ruff) [#1539].
    - Amélioration de la stabilité des builds front-end [#1541, #1522].
- **Optimisation et maintenance** :
    - Optimisation des performances pour éviter les requêtes inutiles (N+1) sur le détail des structures [#1512].
    - Sécurisation du stockage des documents sur S3 via l'ajout de chaînes aléatoires dans les chemins de fichiers [#1481].
    - Correction du processus de nettoyage des documents orphelins pour éviter la perte de documents liés aux services [#1489, #1483].

### Autres changements
- Mise à jour des Conditions Générales d'Utilisation (CGU) et de la politique de confidentialité [#1502].
- Ajout d'une date de mise à jour des données pour plus de transparence [#1500].
- Mise à jour du fichier `security.txt` [#1544].
