## Changelog : nosgestesclimat-app (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une série d'améliorations axées sur l'expérience utilisateur, notamment des corrections de bugs, l'ajout de nouvelles fonctionnalités liées aux actions individuelles pour réduire son impact climatique, et des optimisations techniques pour améliorer la stabilité et la sécurité. L'intégration de nouvelles données et l'amélioration du suivi des actions sont également notables.

### Évolutions fonctionnelles
- **Actions:**
    - Ajout d'un bloc d'actions concrètes à la fin du questionnaire. [#1873](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1873)
    - Améliorations diverses de la présentation et du contenu des actions (wording, impact). [#1835](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1835), [#1849](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1849), [#1822](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1822)
    - Intégration des données d'actions depuis Notion. [#1812](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1812)
    - Possibilité d'évaluer les actions à la fin de la simulation. [#1823](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1823)
- **Questionnaire:**
    - Ajout d'une nouvelle question sur l'âge avec une interface améliorée. [#1788](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1788)
    - Correction du bouton "Passer" pour la question d'âge. [#1838](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1838)
- **Partage:**
    - Correction du partage d'URL avec les paramètres UTM. [#1821](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1821)
- **Interface utilisateur:**
    - Amélioration de l'affichage du graphique des catégories sur la page des résultats groupés. [#1807](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1807)
    - Affichage du formulaire de contact en anglais. [#1853](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1853)
- **Authentification:**
    - Ajout d'une nouvelle stratégie d'authentification interne. [#1883](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1883)
    - Amélioration du processus de vérification du code. [#1813](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1813)

### Évolutions techniques
- **Sécurité:**
    - Correction de vulnérabilités d'open redirect. [#1854](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1854), [#1871](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1871)
    - Suppression d'une directive robots.txt interdisant l'indexation des actions. [#1872](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1872)
- **Infrastructure:**
    - Utilisation de pnpm deploy au lieu de standalone pour la production. [#1831](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1831)
    - Ajout d'un trigger manuel pour le déploiement de l'application. [#1834](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1834)
- **Tests:**
    - Amélioration des tests E2E avec des helpers et des règles ESLint pour les feature flags. [#1840](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1840)
- **Performance:**
    - Ajout d'un worker pour le calcul des actions. [#1811](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1811)
- **Divers:**
    - Mise à jour de la librairie pour la géolocalisation (remplacement de restcountries). [#1847](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1847)
    - Correction de problèmes liés à l'utilisation de cookies en SSR. [#1819](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1819)

### Autres changements
- Correction d'erreurs polluant Sentry. [#1858](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1858)
- Suppression de liens morts. [#1868](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1868), [#1843](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1843)
- Correction d'un bug d'affichage sur Safari pour les modales iframe. [#1870](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1870)
- Suppression du feature flag "mode jeune". [#1874](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1874)
- Correction d'un problème de style avec les boutons des composants serveur. [#1878](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1878)
- Ajout d'une redirection. [#1879](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1879)
- Correction pour autoriser les icônes indéfinies dans les mosaïques numériques. [#1875](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1875)
- Ajout de vérifications pour désactiver les boutons lors de la soumission. [#1842](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1842)
- Correction de la mise à jour du cookie de langue. [#1841](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1841)
- Ajout de la possibilité de définir le mode simulation via l'URL. [#1859](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1859)
- Correction pour permettre le chargement du modèle de nuit. [#1860](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1860)
- Amélioration du suivi automatique (auto-track) pour ignorer le chemin du simulateur et les rageclicks. [#1852](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1852)
- Ajout de migrations pour AnonUser et AnonPoll. [#1856](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1856)
- Amélioration de la visibilité et du SEO de la page de détails des actions. [#1855](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1855)
- Amélioration du texte des services publics sur la page des résultats. [#1851](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1851)
- Ajout de `pollMode` et `organisation` pour afficher AnonPoll. [#1850](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1850)
- Nettoyage et correction de code divers. [#1867](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1867)
