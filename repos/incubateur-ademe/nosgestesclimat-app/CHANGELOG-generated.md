## Changelog : nosgestesclimat-app (30 derniers jours, au 14 juillet 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en matière de sécurité, avec une refonte de l'authentification et la correction de plusieurs vulnérabilités. De nouvelles fonctionnalités ont été ajoutées, notamment un kit de communication et une nouvelle page d'événements. L'expérience utilisateur a également été améliorée grâce à des corrections de bugs et des ajustements d'interface.

### Évolutions fonctionnelles
- Ajout d'un nouveau "Communication Kit" pour faciliter la diffusion d'informations. [#1921](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1921)
- Nouvelle page dédiée aux événements avec une interface améliorée. [#1848](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1848)
- Amélioration de l'affichage du graphique de répartition de l'empreinte carbone. [#1898](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1898)
- Ajout de la possibilité de définir le mode simulation via l'URL. [#1859](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1859)
- Ajout d'illustrations SEDD et modification des chemins des organisations. [#1889](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1889)
- Ajout d'une baseline spécifique pour les jeunes. [#1895](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1895)
- Ajout d'un lien vers l'organisation dans le bloc tutoriel des événements. [#1894](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1894)
- Amélioration de l'affichage du formulaire de contact en anglais. [#1853](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1853)
- Mise à jour du texte des services publics sur la page des résultats. [#1851](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1851)

### Évolutions techniques
- Refonte de la sécurité avec l'implémentation de sessions JOSE et Server Actions, ainsi que la migration des sessions legacy. [#1915](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1915)
- Correction de vulnérabilités d'autorisation et de fuites de données dans les simulations de groupe. [#1885](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1885), [#1923](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1923)
- Correction d'une vulnérabilité d'erreur verbose. [#1871](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1871)
- Correction d'un open redirect. [#1854](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1854)
- Mise à jour de la version du modèle. [#1917](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1917), [#1857](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1857)
- Amélioration de la capture d'erreurs RSC et des erreurs serveur. [#1916](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1916)
- Remplacement de la librairie `restcountries` par un package npm plus maintenu. [#1847](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1847)
- Ajout d'une nouvelle stratégie d'authentification interne. [#1883](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1883)
- Ajout de migrations pour `AnonUser` et `AnonPoll`. [#1856](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1856)

### Autres changements
- Correction de bugs liés à la confirmation de l'inscription à la newsletter. [#1931](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1931)
- Correction de bugs d'affichage de la bannière du kit de communication. [#1928](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1928)
- Correction de bugs de déconnexion avec des sessions legacy. [#1926](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1926)
- Correction de bugs liés au tracking (événements, iframe). [#1911](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1911), [#1900](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1900), [#1852](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1852)
- Suppression de la question d'âge et du test A/B associé. [#1881](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1881)
- Mise à jour de la description des articles de blog. [#1905](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1905)
- Remplacement de "Divers" par "Consommation" dans l'application. [#1904](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1904), [#1897](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1897)
- Amélioration de la réutilisation des composants de test. [#1882](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1882)
- Correction de l'affichage du bouton "Je ne sais pas". [#1875](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1875)
- Suppression d'un lien mort. [#1868](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1868)
- Diverses corrections de style et améliorations de l'interface utilisateur.
