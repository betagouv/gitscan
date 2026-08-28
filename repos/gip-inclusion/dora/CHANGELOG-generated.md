## Changelog : dora (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, le projet a connu une phase importante de restructuration de ses données, notamment pour simplifier la gestion des services et des publics. Parallèlement, l'expérience de recherche a été affinée et de nouveaux outils de notification et d'export ont été ajoutés pour faciliter le travail des gestionnaires et des professionnels.

### Évolutions fonctionnelles
- **Recherche** : Amélioration de l'ergonomie avec la validation par touche Entrée [#1230], limitation du nombre de résultats pour éviter la surcharge [#1245] et suppression automatique des doublons [#1228].
- **Services** : Enrichissement des informations disponibles (nouveaux champs de mobilisation, affichage des précisions sur les publics [#1264]), fusion algorithmique des descriptions de services [#1293] et filtrage du formatage Markdown [#1221].
- **Gestion & Administration** : Mise en place de notifications Slack lors du passage d'une orientation en modération [#1296], accès facilité aux pages d'administration pour les GT [#1286], simplification du tableau de bord des gestionnaires de territoire [#1229] et amélioration de la gestion des erreurs (affichage d'une 404 pour les services inaccessibles [#1224]).
- **Export & Statistiques** : Ajout de la colonne "Identifiant FT" dans les exports d'orientations [#1290] et intégration du stockage des zones géographiques pour les statistiques [#1216].

### Évolutions techniques
- **Refonte du modèle de données** : Migration majeure de la gestion des "Services" et des "Publics" vers un modèle simplifié (passage de relations complexes à des champs uniques ou des tableaux [#1247, #1249, #1252, #1266]) et suppression des anciens schémas et modèles obsolètes [#1279, #1283].
- **Performance & Fiabilité** : Parallélisation des appels API pour accélérer l'édition des services et modèles [#1281], protection contre les suppressions d'objets en cascade [#1220] et renforcement de l'unicité des critères d'admission [#1243].
- **Maintenance** : Correction des URLs vers l'administration Django [#1295], nettoyage des commandes et du code inutilisés [#1260, #1263, #1278, #1285] et ajout d'une commande de normalisation des mots de passe [#1271].

### Autres changements
- **Tests** : Augmentation de la couverture de tests sur les critères d'orientabilité des services [#1227].
