## Changelog : nosgestesclimat-app (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de sécurité, notamment une refonte de l'authentification et la correction de plusieurs vulnérabilités. De nouvelles fonctionnalités ont été ajoutées, comme le catalogue d'actions, le kit de communication et une nouvelle page d'événements, tandis que l'expérience utilisateur a été améliorée grâce à des corrections de bugs et des ajustements d'interface.

### Évolutions fonctionnelles
- Ajout d'un catalogue d'actions publiques [#1845](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1845).
- Implémentation d'un kit de communication [#1896](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1896).
- Nouvelle page dédiée aux événements [#1848](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1848).
- Amélioration de l'affichage du graphique de répartition de l'empreinte carbone [#1898](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1898).
- Ajout d'illustrations SEDD et modification des chemins des organisations [#1889](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1889).
- Ajout d'une baseline spécifique pour les jeunes [#1895](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1895).
- Ajout d'un lien vers l'organisation dans le bloc d'événements [#1894](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1894).
- Correction de l'affichage du bandeau de la campagne partenaire lorsque des simulations sont présentes [#1928](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1928).
- Ajout d'un bloc d'actions sur la page de fin [#1873](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1873).
- Correction du lien "Refaire un test" sur la page "Mon Espace" [#1909](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1909).
- Amélioration du style de la description des articles de blog [#1905](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1905).

### Évolutions techniques
- Refonte de la sécurité : sessions JOSE, Server Actions et migration de l'authentification legacy [#1915](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1915).
- Mise à jour de la version du modèle [#1917](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1917).
- Correction de fuites d'informations dans les simulations de groupe [#1923](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1923).
- Correction de vulnérabilités d'autorisation [#1885](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1885).
- Correction d'un problème de déconnexion avec des sessions legacy [#1926](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1926).
- Correction d'un problème de non-activation du tracking dans les iframes [#1900](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1900).
- Correction d'un problème de mismatch de hooks dans EngineProvider [#1918](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1918).
- Capture systématique des erreurs RSC et des erreurs serveur [#1916](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1916).
- Amélioration de la réutilisation du composant de test de données [#1882](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1882).
- Correction d'une erreur polluant Sentry [#1858](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1858).
- Ajout d'une nouvelle stratégie d'authentification API interne [#1883](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1883).
- Support de postMessage pour React Native WebView dans le flux de partage de données [#1828](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1828).

### Autres changements
- Remplacement de "Divers" par "Consommation" dans plusieurs parties de l'application [#1904](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1904), [#1897](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1897).
- Correction de la confirmation d'inscription à la newsletter [#1931](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1931).
- Correction du style de la page /campagne-partenaire [#1921](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1921).
- Correction du style de la bannière de localisation pour éviter le rognage [#1893](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1893).
- Ajout de traductions manquantes [#1890](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1890).
- Suppression de la page de question d'âge et du test A/B associé [#1881](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1881).
- Correction de la conversion en kg sur la page des résultats du sondage [#1876](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1876).
- Suppression d'un lien mort [#1868](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1868).
- Correction d'une vulnérabilité d'open redirect [#1854](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1854).
- Correction d'une vulnérabilité d'erreur verbose [#1871](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1871).
- Suppression du bouton retour dans la barre supérieure du simulateur [#1891](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1891).
- Mise à jour de la baseline du bouton "Je ne sais pas" [#1892](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1892).
- Correction du style du bouton sur les composants serveur [#1878](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1878).
- Suppression du flag de fonctionnalité "mode jeune" [#1874](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1874).
- Correction de l'affichage des modals iframe pour Safari <= 18 [#1870](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1870).
- Amélioration du workflow de bypass du modal de partage de données [#1869](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1869).
- Correction de l'affichage anonyme [#1867](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1867).
- Ajout de vérifications pour désactiver les boutons lors de la soumission [#1842](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1842).
- Suppression de robots disallow sur les actions [#1872](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1872).
