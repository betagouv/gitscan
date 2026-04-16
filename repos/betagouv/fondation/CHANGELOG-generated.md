## Changelog : fondation (30 derniers jours, au 14 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la gestion des agendas et des nominations, ainsi que sur l'intégration de données provenant de différentes sources (Lolfi et Lodam). Des améliorations significatives ont également été apportées à l'interface utilisateur, notamment au niveau des tableaux de bord et des outils de gestion.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer des agendas et de générer des documents correspondants [#282, #285, #289, #290].
- Amélioration de l'interface de l'agenda avec un affichage plus clair et des fonctionnalités supplémentaires [#300, #301].
- Intégration des données Lolfi pour la création de sessions de nomination [#275, #282].
- Ajout d'indicateurs de priorité (badges) pour les éléments importants [#280].
- Ajout d'une page d'aide Notion pour faciliter l'utilisation de l'application [#294].
- Possibilité d'impersonner des membres pour faciliter le support et la gestion [#287].
- Amélioration de la gestion des rôles, simplifiée pour une meilleure expérience utilisateur [#284].
- Ajout d'alertes lors de l'importation de données Lodam [#277].
- Ajout d'un sélecteur de fichiers utilisant l'ID de fonction [#302].
- Correction de bugs liés à l'affichage du titre du président [#204].
- Correction de bugs liés à la publication des versions de nomination [#000].
- Correction de bugs liés à la disposition des actions dans le tableau des nominations [#299].
- Correction de bugs liés aux tooltips des résultats [#295].

### Évolutions techniques
- Réduction de l'utilisation du réseau lors de l'édition des rapports, améliorant la performance [#298].
- Refactorisation de l'interface utilisateur du tableau de bord des sessions pour une meilleure organisation [#296].
- Migration de la base de données depuis GitHub pour une meilleure gestion et sécurité [#291].
- Ajout d'un diagramme d'architecture au fichier README pour une meilleure compréhension du projet [#286].
- Suppression des alertes Sentry pour les erreurs d'autorisation non autorisées, réduisant le bruit et se concentrant sur les erreurs critiques [#288].
- Suppression de colonnes et tables obsolètes de la base de données [#262].
- Intégration des données Lodam avec Lolfi [#263].
- Installation de Puppeteer pour les fonctionnalités de génération de documents [#208].

### Autres changements
- Ajout de l'internationalisation (i18n) au projet [#303].
- Correction de problèmes liés aux URL des fichiers de nomination Lolfi [#000].
- Correction de problèmes de scaling sur la commande one-off de Scalingo [#000].
- Ajout du titre et du nom d'affichage aux membres [#278].
- Amélioration de l'interface utilisateur de la gestion des sessions [#000].
