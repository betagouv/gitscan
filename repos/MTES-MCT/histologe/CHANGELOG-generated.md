## Changelog : histologe (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité de l'application, la correction de vulnérabilités de sécurité, et l'optimisation des performances, notamment au niveau de la liste des signalements. Des améliorations ont également été apportées à l'interface utilisateur pour faciliter l'utilisation au quotidien des agents.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité pour l'ajout et l'édition d'événements, de documents, de partenaires et de signalements. [#5765, #5781, #5793, #5823]
- Ajout de la possibilité pour les bailleurs d'envoyer des suivis et des documents pendant la procédure de démarche accélérée. [#5819]
- Ajout d'un message informatif pour les logements vacants lors de l'ajout d'un suivi. [#5897]
- Enregistrement du nom du travailleur social dans le formulaire de signalement. [#5867]
- Suppression du blocage du parcours Parc public si le bailleur n'a pas été prévenu ou l'a été trop récemment. [#5854]
- Ajout d'une confirmation lors de la suppression des notifications. [#5800]
- Ajout de liserets pour améliorer la lisibilité du récapitulatif de signalement. [#5865]
- Amélioration de l'affichage des dates et heures des clubs en fonction du fuseau horaire de l'utilisateur sur les emails et le tableau de bord. [#5778]
- Ajout d'un QR code et d'un nombre de recherches sur le service secours. [#5799]
- Correction de la réouverture de la modale de sélection de bâtiment lors d'un changement d'adresse. [#5839]

### Évolutions techniques
- Mise à jour de Twig et Symfony pour corriger des vulnérabilités de sécurité (CVE). [#5887]
- Remplacement du lib php cron par le composant Symfony scheduler. [#5863]
- Montée de version de Doctrine. [#5827]
- Mise à jour de PHPUnit de la version 9 à la version 13. [#5766]
- Suppression ou limitation de l'utilisation des contextes de suivi et des types de suivi. [#5843, #5884]
- Suppression du répertoire `test` lors du déploiement. [#5818]
- Suppression des persist et flush des managers d'entités. [#5757]
- Mise à jour des paquets npm. [#5845, #5893]
- Suppression de la route de gestion des images du firewall principal. [#5891]
- Ajout d'un postmortem pour une vulnérabilité YesWeHack. [#5847]
- Correction d'une vulnérabilité relevée par YesWeHack dans le fichier `.env`. [#5838]
- Ajout de Lighthouse dans la CI pour l'audit de performance. [#5789]
- Utilisation d'un champ dénormalisé `lastSuiviAt` pour améliorer les performances. [#5777]
- Ajout d'un plugin heatmap. [#5718]

### Autres changements
- Amélioration de l'historique des affectations. [#5851]
- Correction de la conversion array to string pour l'envoi de mails. [#5853]
- Diverses modifications de contenu. [#5862]
- Ajout de tests et corrections de fixtures. [#5874]
- Amélioration du tri par code postal sur la liste des territoires. [#5811]
- Ajout de commentaires et nettoyage de code.
- Correction de problèmes d'accessibilité divers. [#5770]
- Suppression de l'affichage de tous les suivis automatiques. [#5795]
- Ajustement du format du numéro de téléphone dans le tooltip des suivis et correction CSS associée. [#5786]
- Amélioration des performances de la liste des signalements et de l'export (ajout du nom des documents et photos). [#5710]
