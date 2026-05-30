## Changelog : histologe (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité de l'application, la correction de vulnérabilités de sécurité, l'optimisation des performances et l'ajout de fonctionnalités pour faciliter le travail des agents, notamment dans la gestion des signalements et des suivis. Des améliorations techniques ont également été apportées pour moderniser l'infrastructure et améliorer la qualité du code.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité pour l'ajout et l'édition d'événements, de documents, et pour les utilisateurs API. [#5765, #5793, #5826]
- Ajout d'un message informatif pour les logements vacants lors de l'ajout d'un suivi de signalement. [#5897]
- Enregistrement du nom du travailleur social lors de la création d'un signalement. [#5867]
- Possibilité pour les bailleurs d'envoyer des suivis et des documents pendant la procédure de démarche accélérée. [#5819]
- Suppression du blocage du parcours "Parc public" si le bailleur n'a pas été prévenu ou l'a été trop récemment. [#5854]
- Ajout d'une confirmation pour vider les notifications dans le back-office. [#5800]
- Ajout de liserets pour améliorer la lisibilité du récapitulatif de signalement. [#5865]
- Ajout du nombre de recherches et du QR code pour le service secours. [#5799]
- Amélioration de l'affichage des affectations dans l'historique. [#5851]
- Ajout d'une fonctionnalité pour masquer les suivis automatiques. [#5795]
- Amélioration du format d'affichage du numéro de téléphone dans les tooltips des suivis. [#5786]

### Évolutions techniques
- Mise à jour de Twig et Symfony pour corriger des vulnérabilités de sécurité (CVE). [#5887]
- Remplacement du lib php cron par le composant Symfony scheduler. [#5863]
- Montée de version de Doctrine. [#5827]
- Mise à jour de PHPUnit de la version 9 à la version 13. [#5766]
- Suppression ou limitation de l'utilisation des contextes de suivi et des types de suivi. [#5843, #5884]
- Suppression du répertoire `test` lors du déploiement. [#5818]
- Suppression des persist et flush des managers d'entités. [#5757]
- Mise à jour des paquets npm. [#5845, #5809]
- Ajout de Lighthouse dans la CI pour l'audit de performance. [#5789]
- Mise à jour de PostCSS. [#5809]
- Ajout d'un postmortem pour une vulnérabilité YesWeHack. [#5847]
- Correction de l'environnement de configuration pour YesWeHack. [#5838]
- Suppression de la route de gestion des images du firewall principal. [#5891]
- Suppression d'une commande temporaire. [#5880]

### Autres changements
- Amélioration de la gestion des fixtures. [#5874]
- Ajout d'une heatmap. [#5718]
- Ancrage de la liste des signalements dans le back-office. [#5868]
- Diverses modifications de contenu. [#5862]
- Correction de bugs et améliorations diverses de l'interface utilisateur. [#5807, #5811, #5770]
- Correction de la conversion array to string pour l'envoi d'emails. [#5853]
- Correction d'un bug lié à la réouverture de la modale de sélection de bâtiment lors d'un changement d'adresse. [#5839]
- Ajout de tri par code postal sur la liste des territoires. [#5811]
- Correction de l'utilisation du champ dénormalisé `lastSuiviAt`. [#5777]
- Configuration de `innodb-buffer-pool-size`. [#5791]
- Désactivation des boutons de soumission pendant les requêtes AJAX. [#5782]
- Correction de problèmes de C/I. [#5765]
