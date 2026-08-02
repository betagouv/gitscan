## Changelog : nosgestesclimat-app (30 derniers jours, au 01 août 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de performance, de sécurité et de fonctionnalités. L'ajout de la gestion des actions personnalisées (i18n) et du catalogue public d'actions sont les évolutions les plus notables pour les utilisateurs, tandis que des optimisations techniques importantes ont été apportées pour améliorer la stabilité et la réactivité de l'application.

### Évolutions fonctionnelles
- Ajout d'un catalogue public d'actions pour réduire son empreinte carbone [#1845](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1845).
- Support de toutes les régions actuelles et précédentes pour les actions [#1961](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1961).
- Ajout d'un bouton de fermeture sur la bannière d'information [#1912](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1912).
- Amélioration de l'affichage du graphique de répartition de l'empreinte carbone et ajout du suivi d'événements [#1898](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1898).
- Mise à jour des mentions "divers" par "consommation" dans l'interface [#1904](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1904).
- Correction de l'affichage de la bannière du kit de communication lors de la présence de simulations [#1928](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1928).
- Correction de l'origine de la confirmation de l'inscription à la newsletter [#1931](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1931).

### Évolutions techniques
- Mise en cache des pages d'accueil et du tutoriel pour les utilisateurs non authentifiés, améliorant significativement les performances [#1946](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1946).
- Ajout d'un reverse proxy Nginx avec cache et limitation de débit pour remplacer un CDN [#1941](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1941).
- Refactorisation du flux de connexion avec une machine à états et des erreurs typées [#1934](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1934).
- Correction d'une fuite de données de simulation en groupe [#1923](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1923).
- Correction de vulnérabilités d'autorisation [#1885](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1885).
- Mise à jour de la version du modèle de calcul d'empreinte carbone [#1917](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1917).
- Correction d'un problème de décalage de compte d'hooks dans le `EngineProvider` [#1918](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1918).
- Capture systématique des erreurs RSC et des erreurs serveur [#1916](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1916).
- Correction d'un problème lié à l'absence de `bilan` [#1884](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1884).
- Suppression d'un en-tête HTTP incorrect dans la configuration Nginx [#1958](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1958).
- Correction d'un problème de déconnexion avec une session héritée [#1926](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1926).
- Correction d'un bug empêchant le bon enregistrement du `referrer` [#1956](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1956).
- Correction d'un test intermittent [#1954](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1954).
- Refonte du sitemap [#1944](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1944).
- Proxification des assets S3 via `/_static/cms` dans Nginx [#1949](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1949).
- Exclusion des redirections `/fr` du cache Nginx [#1947](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1947).
- Nettoyage de la base de données après la fusion de l'i18n des actions [#1943](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1943).
- Ajout de l'i18n pour les actions [#1938](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1938).
- Correction d'un problème de dépassement de mémoire dans les workers de l'environnement de revue [#1940](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1940).

### Autres changements
- Activation du déploiement des actions [#1964](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1964).
- Correction d'un problème d'authentification invalide [#1959](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1959).
- Masquage du bloc d'actions sur la page des résultats liés à l'eau [#1913](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1913).
- Masquage du bloc de communication si l'utilisateur n'est pas administrateur [#1919](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1919).
- Amélioration de la réutilisation du composant de données de test [#1882](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1882).
- Correction du style de la page `/campagne-partenaire` [#1921](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1921).
