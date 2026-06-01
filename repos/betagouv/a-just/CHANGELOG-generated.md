## Changelog : a-just (30 derniers jours, au 31 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur, notamment au niveau du cockpit et du panorama, avec l'ajout d'aide contextuelle et de tests automatisés pour garantir la qualité. Des corrections ont également été apportées pour améliorer la stabilité et la précision des données, en particulier concernant les simulateurs et les effectifs.

### Évolutions fonctionnelles
- Ajout d'un bouton "Qu'est ce que c'est ?" pour les utilisateurs n'ayant pas les droits de modification des ressources humaines, expliquant le ventilateur Human Ressource. [#7141b0fe](https://github.com/betagouv/a-just/commit/7141b0fe)
- Mise à jour de l'aide intégrée (IntroJS) sur les pages panorama et cockpit pour guider les utilisateurs. [#6a786994](https://github.com/betagouv/a-just/commit/6a786994), [#3b7e92a8](https://github.com/betagouv/a-just/commit/3b7e92a8)
- Amélioration de la gestion des dates de début pour les simulateurs. [#4cbe6740](https://github.com/betagouv/a-just/commit/4cbe6740)
- Ajout de tests E2E pour vérifier la complétion des données de contentieux et l'absence d'affichage des contentieux concernés. [#91553eed](https://github.com/betagouv/a-just/commit/91553eed)
- Ajout de tests E2E pour le panorama, notamment pour la vérification des données à compléter. [#fb2a645c](https://github.com/betagouv/a-just/commit/fb2a645c), [#a640a392](https://github.com/betagouv/a-just/commit/a640a392)
- Ajout de tests E2E pour les arrivées et départs dans le module "Changement dans les effectifs". [#a640a392](https://github.com/betagouv/a-just/commit/a640a392)
- Amélioration de l'affichage des messages d'erreur dans les graphiques du cockpit. [#96874250](https://github.com/betagouv/a-just/commit/96874250)

### Évolutions techniques
- Correction de l'accès aux variables d'environnement dans l'API de connexion. [#dadb82f6](https://github.com/betagouv/a-just/commit/dadb82f6), [#5c54f3f1](https://github.com/betagouv/a-just/commit/5c54f3f1), [#74920f8b](https://github.com/betagouv/a-just/commit/74920f8b)
- Mise à jour de la configuration de Cypress pour une meilleure compatibilité. [#5a5144ea](https://github.com/betagouv/a-just/commit/5a5144ea), [#7d27a047](https://github.com/betagouv/a-just/commit/7d27a047), [#8869bca3](https://github.com/betagouv/a-just/commit/8869bca3), [#c76918ac](https://github.com/betagouv/a-just/commit/c76918ac)
- Correction de bugs et améliorations diverses dans les tests E2E. [#4727e4ed](https://github.com/betagouv/a-just/commit/4727e4ed), [#b6bb7e28](https://github.com/betagouv/a-just/commit/b6bb7e28), [#ea7ec942](https://github.com/betagouv/a-just/commit/ea7ec942)
- Correction de la configuration de Redis pour un redémarrage automatique. [#9ebdd611](https://github.com/betagouv/a-just/commit/9ebdd611)
- Correction de la migration des décharges syndicales. [#adb7bc4c](https://github.com/betagouv/a-just/commit/adb7bc4c)
- Mise à jour des dépendances et des fichiers de verrouillage. [#ced7d647](https://github.com/betagouv/a-just/commit/ced7d647)

### Autres changements
- Correction de scripts JavaScript. [#5a8c4c9d](https://github.com/betagouv/a-just/commit/5a8c4c9d)
- Suppression de code inutilisé. [#48dba93f](https://github.com/betagouv/a-just/commit/48dba93f)
- Ajout de règles ASA (Absence pour Suivi d'Aptitude). [#9d12076f](https://github.com/betagouv/a-just/commit/9d12076f)
- Migration ASA vers l'absentéisme. [#53231a9d](https://github.com/betagouv/a-just/commit/53231a9d)
- Ajout de tooltips EPT au calculateur. [#598f8aa3](https://github.com/betagouv/a-just/commit/598f8aa3)
- Amélioration de la gestion des alertes EPT dans le cockpit. [#d4f5814e](https://github.com/betagouv/a-just/commit/d4f5814e)
- Correction de bugs mineurs et amélioration de la lisibilité du code. [#2f5e5b6c](https://github.com/betagouv/a-just/commit/2f5e5b6c), [#384acf90](https://github.com/betagouv/a-just/commit/384acf90), [#255ea8da](https://github.com/betagouv/a-just/commit/255ea8da)
- Ajout d'un fichier `.env.example` pour les tests E2E. [#aa479cde](https://github.com/betagouv/a-just/commit/aa479cde)
- Correction d'erreurs grammaticales dans les logs. [#384acf90](https://github.com/betagouv/a-just/commit/384acf90)
- Ajout de logs au cockpit. [#255ea8da](https://github.com/betagouv/a-just/commit/255ea8da)
