## Changelog : espace-membre-next (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'accessibilité, la correction de bugs et l'ajout de nouvelles fonctionnalités pour faciliter la gestion des startups et des phases de projets. Des efforts ont également été faits pour simplifier le code et améliorer la performance de l'application.

### Évolutions fonctionnelles
- **Recherche de startups :** Ajout d'un champ de recherche combiné pour faciliter la recherche de startups. [#1324](https://github.com/betagouv/espace-membre-next/issues/1324)
- **Gestion des phases :** Amélioration de la gestion des phases de projet. [#1304](https://github.com/betagouv/espace-membre-next/issues/1304)
- **Edition des membres par les agents startup :** Les agents des startups peuvent désormais éditer les informations des membres. [#1303](https://github.com/betagouv/espace-membre-next/issues/1303)
- **Onboarding :**  Les attributaires ne se voient plus créer d'email lors de l'onboarding. [#1305](https://github.com/betagouv/espace-membre-next/issues/1305)
- **Création d'email :** Correction d'un bug empêchant la création d'email lorsque l'email principal n'est pas défini. [#1342](https://github.com/betagouv/espace-membre-next/issues/1342)

### Évolutions techniques
- **Accessibilité (RGAA) :** Améliorations significatives de l'accessibilité, notamment l'ajout de l'attribut `lang` sur la balise `<html>`, la correction de problèmes d'accessibilité des labels et des éléments cliquables, et l'activation du preset recommandé `jsx-a11y`. [#1365](https://github.com/betagouv/espace-membre-next/issues/1365), [#1361](https://github.com/betagouv/espace-membre-next/issues/1361), [#1363](https://github.com/betagouv/espace-membre-next/issues/1363), [#1364](https://github.com/betagouv/espace-membre-next/issues/1364)
- **Sécurité :** Renforcement de la sécurité en appliquant une vérification d'authentification dans la fonction `updateUserEvent`. [#1357](https://github.com/betagouv/espace-membre-next/issues/1357)
- **Migration MJML :** Migration du système de template email vers MJML. [#1350](https://github.com/betagouv/espace-membre-next/issues/1350)
- **Simplification du routage :** Simplification du routage et utilisation accrue du rendu côté serveur (SSR). [#1326](https://github.com/betagouv/espace-membre-next/issues/1326)
- **Refactoring :** Suppression de code obsolète lié à Mattermost, de variables d'environnement inutiles et de composants DSFR obsolètes. [#1325](https://github.com/betagouv/espace-membre-next/issues/1325), [#1329](https://github.com/betagouv/espace-membre-next/issues/1329), [#1351](https://github.com/betagouv/espace-membre-next/issues/1351)
- **Timeouts :** Augmentation du timeout pour la synchronisation des emails. [#1372](https://github.com/betagouv/espace-membre-next/issues/1372)

### Autres changements
- **Tests E2E :** Ajout de tests end-to-end (E2E) pour le tableau de bord et les processus d'onboarding/offboarding. [#1299](https://github.com/betagouv/espace-membre-next/issues/1299)
- **Nettoyage :** Suppression de code et de configurations inutiles. [#1331](https://github.com/betagouv/espace-membre-next/issues/1331), [#1337](https://github.com/betagouv/espace-membre-next/issues/1337), [#1338](https://github.com/betagouv/espace-membre-next/issues/1338), [#1339](https://github.com/betagouv/espace-membre-next/issues/1339), [#1374](https://github.com/betagouv/espace-membre-next/issues/1374), [#1375](https://github.com/betagouv/espace-membre-next/issues/1375)
- **Logging :** Correction de problèmes de logging. [#1302](https://github.com/betagouv/espace-membre-next/issues/1302)
