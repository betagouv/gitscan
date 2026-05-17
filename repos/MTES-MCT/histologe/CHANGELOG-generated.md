## Changelog : histologe (30 derniers jours, au 13 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives en termes d'accessibilité, de performance et de correction de vulnérabilités. Des efforts ont été déployés pour améliorer l'expérience utilisateur dans l'interface d'administration (BO), notamment au niveau du tableau de bord et de la gestion des signalements. Des optimisations techniques ont également été réalisées pour renforcer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité générale de l'application, notamment pour les utilisateurs API, les événements, les documents, les partenaires et le tableau de bord. [#5826, #5793, #5781, #5734, #5732]
- Ajout d'une confirmation lors de la suppression des notifications dans l'interface d'administration. [#5800]
- Ajout de l'heure dans le suivi des visites programmées. [#5759]
- Ajout de filtres pour les événements. [#5713, #5740]
- Amélioration de l'affichage de la date/heure des clubs dans les emails et le tableau de bord, en tenant compte du fuseau horaire de l'utilisateur. [#5778, #5785]
- Correction de la réouverture de la modale de sélection de bâtiment lors d'un changement d'adresse dans l'interface de signalement. [#5839]
- Correction de la conversion d'un tableau en chaîne de caractères pour l'envoi d'emails. [#5853]
- Ajout du nom des documents et des photos lors de l'export des signalements. [#5710]
- Correction de l'affichage du numéro de téléphone dans le tooltip des suivis. [#5786, #5788]

### Évolutions techniques
- Mise à jour de plusieurs dépendances : PHPUnit (version 9 vers 13), PostCSS, Axios, Doctrine. [#5766, #5809, #5827, #5824]
- Remplacement de la librairie phpspreadsheets par une alternative. [#5836]
- Suppression des persist et flush des managers d'entités pour optimiser les performances. [#5757]
- Correction d'une vulnérabilité relevée par YesWeHack et ajout d'un postmortem. [#5847, #5838]
- Mise à jour de la configuration Nginx. [#5739]
- Suppression du répertoire `test` lors du déploiement. [#5818]
- Déplacement de la logique d'update et de nettoyage vers les classes Behaviour dans plusieurs repositories. [#5762]
- Ajout de Lighthouse dans la CI pour l'audit de performance. [#5789]
- Optimisation du comptage pour le panneau des dossiers fermés par les communes. [#5735, #5736]
- Désactivation des boutons de soumission lors des requêtes AJAX pour éviter les soumissions multiples. [#5782, #5790]

### Autres changements
- Mise à jour de la collection Postman. [#5830, #5831]
- Correction de la pagination des connexions SI. [#5755, #5758]
- Gestion des messages de resynchronisation. [#5754, #5756]
- Préservation des données EXIF des photos. [#5702]
- Suppression des auto-suivis cachés. [#5795, #5798]
- Configuration de `innodb-buffer-pool-size`. [#5791, #5792]
- Amélioration du formatage du code et correction de problèmes de CI/C. [#5765, #5770, #5812]
