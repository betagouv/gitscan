## Changelog : espace-membre-next (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la recherche de startups et de la gestion des phases. Des corrections importantes ont également été apportées pour améliorer l'accessibilité (RGAA) et la sécurité de la plateforme. Enfin, plusieurs optimisations et suppressions de code obsolète ont été réalisées.

### Évolutions fonctionnelles
- **Recherche de startups:** Ajout d'un champ de recherche combiné pour faciliter la recherche de startups. [#1324](https://github.com/betagouv/espace-membre-next/issues/1324)
- **Gestion des phases:** Amélioration de la gestion des phases, avec des noms et libellés alignés sur beta.gouv.fr. [#1384](https://github.com/betagouv/espace-membre-next/issues/1384) et [#1304](https://github.com/betagouv/espace-membre-next/issues/1304)
- **Gestion des événements:** Correction des noms des événements dans la gestion des startups. [#1385](https://github.com/betagouv/espace-membre-next/issues/1385)
- **Emails:** Correction d'un bug empêchant la création d'emails lorsque l'adresse email principale n'est pas définie. [#1342](https://github.com/betagouv/espace-membre-next/issues/1342)

### Évolutions techniques
- **Accessibilité (RGAA):** Améliorations significatives de l'accessibilité, incluant l'ajout de l'attribut `lang` sur la balise `<html>`, le remplacement de labels orphelins et le rendu des éléments cliquables accessibles au clavier. [#1361](https://github.com/betagouv/espace-membre-next/issues/1361), [#1363](https://github.com/betagouv/espace-membre-next/issues/1363), [#1364](https://github.com/betagouv/espace-membre-next/issues/1365)
- **Sécurité:** Renforcement de la sécurité en appliquant une vérification d'authentification lors de la mise à jour des événements. [#1357](https://github.com/betagouv/espace-membre-next/issues/1357)
- **Migration MJML:** Migration du système d'emails vers MJML. [#1350](https://github.com/betagouv/espace-membre-next/issues/1350)
- **Refactoring & Optimisations:** Simplification du routage et utilisation accrue du rendu côté serveur (SSR) pour améliorer les performances. [#1326](https://github.com/betagouv/espace-membre-next/issues/1326)
- **Suppression de code obsolète:** Suppression de code lié à Mattermost, ainsi que des configurations inutiles. [#1325](https://github.com/betagouv/espace-membre-next/issues/1325), [#1375](https://github.com/betagouv/espace-membre-next/issues/1375)
- **DSFR:** Mise à jour pour utiliser le composant `DataVisualization` au lieu d'un asset SVG supprimé. [#1351](https://github.com/betagouv/espace-membre-next/issues/1351)
- **Timeouts:** Augmentation du timeout pour la synchronisation des emails. [#1372](https://github.com/betagouv/espace-membre-next/issues/1372)

### Autres changements
- **Documentation:** Renommage et documentation de la tâche `phase-reminder`. [#1374](https://github.com/betagouv/espace-membre-next/issues/1374)
- **Nettoyage:** Suppression de variables d'environnement inutiles et de configurations obsolètes. [#1329](https://github.com/betagouv/espace-membre-next/issues/1329), [#1339](https://github.com/betagouv/espace-membre-next/issues/1339)
- **Configuration:** Suppression de la configuration dotenv. [#1337](https://github.com/betagouv/espace-membre-next/issues/1337)
- **Mises à jour:** Quelques mises à jour de dépendances. [#1331](https://github.com/betagouv/espace-membre-next/issues/1331)
- **Sécurité:** Suppression d'un TODO concernant l'authentification dans `validateNewMember`. [#1354](https://github.com/betagouv/espace-membre-next/issues/1354)
- **Tests:** Activation du preset recommandé jsx-a11y pour les tests. [#1355](https://github.com/betagouv/espace-membre-next/issues/1355)
