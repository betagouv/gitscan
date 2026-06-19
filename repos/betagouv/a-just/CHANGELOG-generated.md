## Changelog : a-just (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur la page Panorama avec l'ajout de tests E2E et l'amélioration de l'interface pour la saisie de dates. Des corrections et des améliorations ont également été apportées au cockpit, notamment pour le calcul des entrées/sorties et l'affichage des données. Des mises à jour des fichiers de nomenclature et des correctifs liés aux extracteurs de données ont également été intégrés.

### Évolutions fonctionnelles
- Amélioration de la saisie de dates : Possibilité d'entrer manuellement les dates dans les composants `aj-date-select` et `aj-date-select-blue` tout en conservant l'utilisation du sélecteur de date. [#761752ed](https://github.com/betagouv/a-just/commit/761752ed)
- Amélioration de l'interface Panorama :
    - Ajout de tests E2E pour valider le fonctionnement de la page. [#57939669](https://github.com/betagouv/a-just/commit/57939669)
    - Mise à jour du texte du guide d'utilisation (étape 5). [#41f42fc2](https://github.com/betagouv/a-just/commit/41f42fc2)
    - Ajout de tooltips pour le graphique du cockpit. [#ddffd4cb](https://github.com/betagouv/a-just/commit/ddffd4cb)
    - Ajout d'un bouton "Qu'est ce que c'est ?" caché pour les utilisateurs sans droit de modification des ressources humaines. [#7141b0fe](https://github.com/betagouv/a-just/commit/7141b0fe) et [#de0f0288](https://github.com/betagouv/a-just/commit/de0f0288)
    - Mise à jour de l'étape par étape (IntroJS) sur la page du cockpit. [#3b7e92a8](https://github.com/betagouv/a-just/commit/3b7e92a8)
- Amélioration du cockpit :
    - Ajout de la gestion des "Entrées" et "Sorties" dans le composant `ReferentielCalculatorComponent`. [#7f9788c3](https://github.com/betagouv/a-just/commit/7f9788c3)
    - Correction de l'affichage de la première date dans le futur. [#c46e98e4](https://github.com/betagouv/a-just/commit/c46e98e4) et [#66dc8923](https://github.com/betagouv/a-just/commit/66dc8923)
- Mise à jour des fichiers de nomenclature. [#09f0d356](https://github.com/betagouv/a-just/commit/09f0d356)
- Correction de la migration des décharges syndicales. [#adb7bc4c](https://github.com/betagouv/a-just/commit/adb7bc4c)

### Évolutions techniques
- Refactorisation des workflows GitHub Actions pour simplifier les déploiements. [#2ce96a06](https://github.com/betagouv/a-just/commit/2ce96a06)
- Mise à jour de la configuration Cypress. [#e67c7077](https://github.com/betagouv/a-just/commit/e67c7077)
- Correction de tests E2E et ajout de nouveaux tests pour la page Panorama et le cockpit. [#1fde3081](https://github.com/betagouv/a-just/commit/1fde3081), [#403bb79b](https://github.com/betagouv/a-just/commit/403bb79b), [#a640a392](https://github.com/betagouv/a-just/commit/a640a392)
- Suppression de fichiers et de configurations inutilisés. [#b1db5b53](https://github.com/betagouv/a-just/commit/b1db5b53)
- Mise à jour de la gestion des variables d'environnement dans les tests E2E. [#aa2b3cd5](https://github.com/betagouv/a-just/commit/aa2b3cd5)
- Correction de problèmes de chargement dans le composant `PopinEditActivitiesComponent`. [#8bb98145](https://github.com/betagouv/a-just/commit/8bb98145)
- Ajout de la sécurité CSP. [#88bcc8ef](https://github.com/betagouv/a-just/commit/88bcc8ef) et [#4cc7bcff](https://github.com/betagouv/a-just/commit/4cc7bcff) et [#d5fe214e](https://github.com/betagouv/a-just/commit/d5fe214e)

### Autres changements
- Suppression de commentaires et de logs inutiles. [#a9b5435b](https://github.com/betagouv/a-just/commit/a9b5435b), [#2a7da289](https://github.com/betagouv/a-just/commit/2a7da289), [#32a0f972](https://github.com/betagouv/a-just/commit/32a0f972), [#8223a9b1](https://github.com/betagouv/a-just/commit/8223a9b1)
- Ajout du nom de l'agent à l'usage. [#cc8242bc](https://github.com/betagouv/a-just/commit/cc8242bc)
- Correction de la catégorisation ASA. [#9e73db5c](https://github.com/betagouv/a-just/commit/9e73db5c)
- Correction de l'appel de script JS. [#5a8c4c9d](https://github.com/betagouv/a-just/commit/5a8c4c9d)
- Correction de l'affectation de la catégorie d'agent au simulateur. [#40cd7aa1](https://github.com/betagouv/a-just/commit/40cd7aa1)
- Redémarrage automatique de Redis dans Docker. [#9ebdd611](https://github.com/betagouv/a-just/commit/9ebdd611)
- Correction du fichier excel extracteur-collecte 2026. [#216bf323](https://github.com/betagouv/a-just/commit/216bf323)
- Migration ASA vers absenteisme. [#53231a9d](https://github.com/betagouv/a-just/commit/53231a9d)
