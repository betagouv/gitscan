## Changelog : nosgestesclimat-app (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une refonte de la sécurité avec l'implémentation de sessions JOSE et de Server Actions, améliorant ainsi la protection des données utilisateurs. Plusieurs améliorations ont été apportées à l'expérience utilisateur, notamment sur les pages d'événements, de résultats et le flux de partage de données. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- **CommunicationKit intégré** : Ajout d'un nouveau kit de communication pour améliorer l'engagement des utilisateurs. [#1896](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1896)
- **Page d'événements améliorée** : Nouvelle page d'événements avec une présentation plus claire et des informations plus complètes. [#1848](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1848)
- **Amélioration de la page de fin de simulation** : Ajout de blocs d'actions et amélioration du style pour les petits écrans. [#1899](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1899), [#1873](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1873)
- **Partage de données simplifié** : Amélioration du flux de partage de données, notamment avec le support de React Native WebView et une vérification par clé. [#1828](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1828), [#1869](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1869)
- **Nouvelle baseline pour les jeunes** : Ajout d'une baseline spécifique pour les jeunes dans le simulateur. [#1895](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1895)
- **Amélioration des illustrations SEDD** : Ajout d'illustrations SEDD et modification des chemins des organisations. [#1889](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1889)
- **Amélioration du style des descriptions d'articles de blog** : Amélioration de la présentation des descriptions d'articles de blog. [#1905](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1905)
- **Prise en charge du mode simulation via URL** : Possibilité de définir le mode simulation directement depuis l'URL. [#1859](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1859)
- **Chargement du modèle de nuit** : Correction permettant le chargement du modèle de nuit. [#1860](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1860)

### Évolutions techniques
- **Refonte de la sécurité** : Implémentation de sessions JOSE et de Server Actions pour une meilleure sécurité. [#1915](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1915)
- **Gestion des erreurs améliorée** : Capture systématique des erreurs RSC et des erreurs serveur. [#1916](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1916)
- **Nouvelle stratégie d'authentification interne** : Ajout d'une nouvelle stratégie d'authentification interne. [#1883](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1883)
- **Suppression de la question d'âge** : Suppression de la page de question d'âge et du test A/B associé. [#1881](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1881)
- **Mise à jour de la version du modèle** : Mise à jour de la version du modèle utilisé pour les calculs. [#1857](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1857)
- **Remplacement de restcountries** : Remplacement de la librairie restcountries par un package npm plus maintenu. [#1847](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1847)
- **Amélioration de la gestion des erreurs dans les composants serveur** : Correction d'un problème de style dans les composants serveur. [#1878](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1878)

### Autres changements
- **Corrections de bugs** : Plusieurs corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de l'application, notamment concernant le suivi des événements, les iframes sur Safari, et les calculs de conversion. [#1918](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1918), [#1900](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1900), [#1876](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1876), [#1870](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1870)
- **Amélioration de la documentation** : Ajout de traductions manquantes. [#1890](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1890)
- **Nettoyage du code** : Suppression de liens morts et de code obsolète. [#1868](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1868), [#1858](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1858)
- **Correction de vulnérabilités de sécurité** : Correction de vulnérabilités de sécurité potentielles. [#1871](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1871), [#1854](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1854)
