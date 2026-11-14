## Changelog : dora (30 derniers jours, au 13 novembre 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une refonte de sa page d'accueil et d'une amélioration significative de son moteur de recherche. Nous avons également renforcé la sécurité globale du système et fiabilisé la gestion des documents et des données utilisateurs pour garantir une expérience plus stable et sécurisée.

### Évolutions fonctionnelles
- **Interface et navigation** : Refonte de la page d'accueil avec une navigation par onglets adaptée à chaque public [#1449](https://github.com/gip-inclusion/dora/issues/1449), simplification de l'affichage des détails des structures [#1385](https://github.com/gip-inclusion/dora/issues/1385) et pré-sélection automatique du formulaire Dora pour les services [#1462](https://github.com/gip-inclusion/dora/issues/1462).
- **Recherche** : Remplacement de la recherche Google par la recherche par mots-clés native de Dora [#1464](https://github.com/gip-inclusion/dora/issues/1464) et partage du dernier lieu sélectionné entre la recherche thématique et la recherche par mots-clés [#1476](https://github.com/gip-inclusion/dora/issues/1476).
- **Expérience utilisateur** : Nouvelle notice pour le chargement des documents [#1482](https://github.com/gip-inclusion/dora/issues/1482), redirection des demandes d'orientation vers la plateforme de l'inclusion [#1463](https://github.com/gip-inclusion/dora/issues/1463) et ajout d'une date de mise à jour des données pour plus de transparence [#1500](https://github.com/gip-inclusion/dora/issues/1500).
- **Corrections** : Gestion des doublons lors de l'acceptation des adhésions [#1509](https://github.com/gip-inclusion/dora/issues/1509), masquage des options de sauvegarde pour les utilisateurs déconnectés [#1511](https://github.com/gip-inclusion/dora/issues/1511), fiabilisation de l'importation des utilisateurs [#1471](https://github.com/gip-inclusion/dora/issues/1471) et correction des erreurs de statistiques liées à des champs invalides [#1454](https://github.com/gip-inclusion/dora/issues/1454).

### Évolutions techniques
- **Sécurité** : Renforcement de la politique de sécurité du contenu (CSP) et des en-têtes de sécurité [#1530](https://github.com/gip-inclusion/dora/issues/1530), suppression d'endpoints de diagnostic non sécurisés [#1477](https://github.com/gip-inclusion/dora/issues/1477), [#1480](https://github.com/gip-inclusion/dora/issues/1480) et sécurisation des accès aux uploads [#1478](https://github.com/gip-inclusion/dora/issues/1478).
- **Performance et architecture** : Optimisation des requêtes pour le détail des structures (évitement du problème N+1) [#1512](https://github.com/gip-inclusion/dora/issues/1512) et refactorisation des gestionnaires de services [#1496](https://github.com/gip-inclusion/dora/issues/1496).
- **Intégrité des données** : Correction de la suppression accidentelle de documents lors du nettoyage des fichiers orphelins [#1483](https://github.com/gip-inclusion/dora/issues/1483), [#1489](https://github.com/gip-inclusion/dora/issues/1489) et nettoyage des références aux pièces jointes absentes du stockage [#1452](https://github.com/gip-inclusion/dora/issues/1452).
- **Infrastructure et CI/CD** : Ajout d'un workflow de relecture automatique des Pull Requests [#1497](https://github.com/gip-inclusion/dora/issues/1497), amélioration de la vérification des builds frontend [#1522](https://github.com/gip-inclusion/dora/issues/1522) et stabilisation de l'outil d'analyse DuckDB [#1521](https://github.com/gip-inclusion/dora/issues/1521).
- **Stockage** : Sécurisation et unicité des chemins de stockage des documents sur S3 via l'ajout de chaînes aléatoires [#1481](https://github.com/gip-inclusion/dora/issues/1481).

### Autres changements
- Mise à jour des Conditions Générales d'Utilisation (CGU) et de la politique de confidentialité [#1502](https://github.com/gip-inclusion/dora/issues/1502).
- Mise à jour du fichier `security.txt` [#1493](https://github.com/gip-inclusion/dora/issues/1493).
