## Changelog : rdv-service-public (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la migration vers un nouveau nom de domaine, l'amélioration de l'expérience utilisateur notamment pour les rendez-vous collectifs et la synchronisation CalDAV, ainsi que des corrections de bugs et des optimisations techniques. Des améliorations ont également été apportées à l'interface d'administration pour faciliter la gestion des services et des motifs de rendez-vous.

### Évolutions fonctionnelles
- **Nouveau nom de domaine :** Adaptation de l'application au nouveau nom de domaine, incluant la redirection, la documentation et les rendez-vous d'accompagnement. [#6480](https://github.com/betagouv/rdv-service-public/issues/6480), [#6481](https://github.com/betagouv/rdv-service-public/issues/6481), [#6479](https://github.com/betagouv/rdv-service-public/issues/6479)
- **Rendez-vous collectifs :** Amélioration de l'interface pour la création de rendez-vous collectifs, avec l'utilisation de cartes DSFR pour les choix de motifs. [#6448](https://github.com/betagouv/rdv-service-public/issues/6448)
- **Synchronisation CalDAV :** Correction de bugs et ajout d'étapes pour améliorer la synchronisation CalDAV, notamment avec Zimbra. [#6416](https://github.com/betagouv/rdv-service-public/issues/6416), [#6417](https://github.com/betagouv/rdv-service-public/issues/6417), [#6172](https://github.com/betagouv/rdv-service-public/issues/6172)
- **Interface agent :** Utilisation de cartes DSFR dans la recherche de créneaux côté agents. [#6437](https://github.com/betagouv/rdv-service-public/issues/6437)
- **Inscription usager :** Redirection vers la liste des créneaux collectifs après l'inscription d'un usager. [#6469](https://github.com/betagouv/rdv-service-public/issues/6469)
- **Gestion des services :** Les administrateurs d'espace peuvent désormais créer un nouveau service. [#6455](https://github.com/betagouv/rdv-service-public/issues/6455)
- **Motifs de rendez-vous :** Ajout d'une interface pour créer 29 motifs France Service en un clic. [#6406](https://github.com/betagouv/rdv-service-public/issues/6406)
- **Amélioration de l'expérience utilisateur :** Ajout d'instructions pour les usagers lors de la réservation en ligne. [#6431](https://github.com/betagouv/rdv-service-public/issues/6431)

### Évolutions techniques
- **Refactoring CSS :** Réduction de la dépendance à Bootstrap en utilisant des classes CSS personnalisées. [#6457](https://github.com/betagouv/rdv-service-public/issues/6457)
- **Composants DSFR :** Remplacement progressif des composants Bootstrap par des composants Design System Français (DSFR) : badges, boutons, cards, accordéon. [#6467](https://github.com/betagouv/rdv-service-public/issues/6467), [#6468](https://github.com/betagouv/rdv-service-public/issues/6468), [#6434](https://github.com/betagouv/rdv-service-public/issues/6434)
- **Mise à jour de Puma :** Mise à jour de la version de Puma à 7.2.1. [#6425](https://github.com/betagouv/rdv-service-public/issues/6425)
- **Sécurité :** Fixation des versions des actions GitHub par hash pour renforcer la sécurité. [#6412](https://github.com/betagouv/rdv-service-public/issues/6412)
- **GoodJob :** Correction d'un problème lié à la gestion des jobs GoodJob. [#6408](https://github.com/betagouv/rdv-service-public/issues/6408)
- **Tests :** Amélioration de la stabilité des tests, notamment en corrigeant des flaky specs. [#6426](https://github.com/betagouv/rdv-service-public/issues/6426), [#6411](https://github.com/betagouv/rdv-service-public/issues/6411), [#6453](https://github.com/betagouv/rdv-service-public/issues/6453)

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter le nouveau nom de domaine. [#6480](https://github.com/betagouv/rdv-service-public/issues/6480)
- **Configuration :** Ajout d'une variable d'environnement pour afficher les login codes sur les review apps. [#6454](https://github.com/betagouv/rdv-service-public/issues/6454)
- **Nettoyage de code :** Suppression de code inutilisé et de commentaires obsolètes. [#6423](https://github.com/betagouv/rdv-service-public/issues/6423), [#6445](https://github.com/betagouv/rdv-service-public/issues/6445)
- **Correction de bugs mineurs :** Diverses corrections de bugs, notamment liés à l'annulation de rendez-vous, aux erreurs CalDAV et à l'affichage de messages d'erreur. [#6478](https://github.com/betagouv/rdv-service-public/issues/6478), [#6470](https://github.com/betagouv/rdv-service-public/issues/6470), [#6409](https://github.com/betagouv/rdv-service-public/issues/6409)
