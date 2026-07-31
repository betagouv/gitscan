## Changelog : nosgestesclimat-app (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de la sécurité, notamment une refonte complète de la gestion des sessions et de l'authentification. Des optimisations de performance ont également été apportées grâce à la mise en cache de certaines pages et à l'amélioration de la gestion des assets. Plusieurs corrections de bugs et améliorations de l'expérience utilisateur ont été implémentées, notamment concernant l'affichage des bannières, des actions et des résultats.

### Évolutions fonctionnelles
- Ajout d'un bouton de fermeture sur les bannières [#1912](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1912).
- Publication du catalogue public d'actions [#1845](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1845).
- Réactivation des actions liées aux services sociétaux [#1955](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1955).
- Amélioration de l'affichage et du suivi des données de la répartition de l'empreinte carbone [#1898](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1898).
- Ajout du Communication Kit [#1896](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1896).
- Mise à jour de la version du modèle de calcul [#1917](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1917).
- Correction de l'affichage de la bannière du kit de communication lors de la présence de simulations [#1928](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1928).
- Amélioration de la réutilisation du composant de données de test [#1882](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1882).

### Évolutions techniques
- Refonte de la sécurité : sessions JOSE, Server Actions et migration de l'ancien système [#1915](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1915).
- Mise en cache des pages d'accueil et du tutoriel pour les utilisateurs non authentifiés [#1946](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1946).
- Ajout d'un reverse proxy Nginx avec cache et limitation de débit [#1941](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1941).
- Proxy des assets S3 via `/_static/cms` dans Nginx [#1949](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1949).
- Typage des erreurs d'authentification et utilisation de `ts-pattern` [#1942](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1942).
- Refactorisation du flux de connexion avec une machine à états et des erreurs typées [#1934](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1934).
- Correction d'une fuite de données de simulation de groupe [#1923](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1923).
- Correction de vulnérabilités d'autorisation [#1885](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1885).
- Correction d'un problème de comptage de hooks dans `EngineProvider` [#1918](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1918).
- Capture systématique des erreurs RSC et des erreurs serveur [#1916](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1916).
- Suppression d'un en-tête `Host` incorrect dans la configuration Nginx [#1958](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1958).

### Autres changements
- Correction de l'origine de la confirmation de l'inscription à la newsletter [#1931](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1931).
- Mise à jour des mentions "divers" en "consommation" [#1904](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1904).
- Correction d'un problème de déconnexion avec une session legacy [#1926](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1926).
- Correction d'un bug lié à la définition de l'URL de référence dans PostHog [#1956](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1956).
- Nettoyage de la base de données après la fusion des actions i18n [#1943](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1943).
- Correction d'un test flaky [#1954](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1954).
- Refonte du sitemap [#1944](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1944).
- Correction d'un problème d'erreur 500 en production [#1940](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1940).
- Correction d'un problème d'affichage du lien vers le nouveau test sur la page "Mon Espace" [#1909](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1909).
- Amélioration du style de la page de fin [#1899](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1899).
- Amélioration du style de la description des articles de blog [#1905](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1905).
- Correction de l'affichage du style de la page partenaire [#1921](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1921).
- Ajout d'un logo dans la barre supérieure des tests [#1902](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1902).
- Correction d'un problème lié à l'absence de referrer [#1911](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1911).
- Correction d'un problème lié à la gestion des bilans `undefined` [#1884](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1884).
- Correction d'un problème d'affichage du bloc d'actions sur la page des résultats eau [#1913](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1913).
- Masquage du bloc d'actions si l'utilisateur n'est pas administrateur [#1919](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1919).
- Tentative de correction des codes d'authentification invalides [#1959](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1959).
