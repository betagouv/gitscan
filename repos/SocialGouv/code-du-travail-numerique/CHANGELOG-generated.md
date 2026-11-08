## Changelog : code-du-travail-numerique (30 derniers jours, au 05 novembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la visibilité du contenu (SEO et métadonnées), l'enrichissement de l'expérience utilisateur sur les actualités et les fiches de service, ainsi que sur le renforcement de la stabilité technique (sécurité, CI/CD et observabilité).

### Évolutions fonctionnelles
- **Actualités** : Amélioration de l'affichage avec l'ajout de la date de publication, des images, ainsi que des sections « Pour aller plus loin » et « Références » ([#7553](https://github.com/SocialGouv/code-du-travail-numerique/issues/7553)).
- **Contributions** : Ajout d'une introduction pour faciliter la compréhension des conventions collectives ([#7567](https://github.com/SocialGouv/code-du-travail-numerique/issues/7567)).
- **Fiches Service-Public** : Intégration de liens recommandés vers les contenus internes et ajout de l'événementiel Matomo ([#7544](https://github.com/SocialGouv/code-du-travail-numerique/issues/7544)).
- **Correction** : Correction de la redirection du bouton d'indemnité de départ à la retraite vers le simulateur ([#7561](https://github.com/SocialGouv/code-du-travail-numerique/issues/7561)).

### Évolutions techniques
- **Optimisation SEO** : 
    - Amélioration massive des métadonnées (JSON-LD, Open Graph, flux RSS) et gestion des logos ([#7548](https://github.com/SocialGouv/code-du-travail-numerique/issues/7548), [#7569](https://github.com/SocialGouv/code-du-travail-numerique/issues/7569), [#7572](https://github.com/SocialGouv/code-du-travail-numerique/issues/7572)).
    - Correction des redirections 301 et du format des URLs pour les congés pour événements familiaux ([#7580](https://github.com/SocialGouv/code-du-travail-numerique/issues/7580), [#7582](https://github.com/SocialGouv/code-du-travail-numerique/issues/7582)).
    - Tests d'amélioration du SEO sur les contributions ([#7511](https://github.com/SocialGouv/code-du-travail-numerique/issues/7511)).
- **Infrastructure et Sécurité** :
    - Mise à jour de Node.js pour intégrer les correctifs de sécurité d'octobre 2026 ([#7571](https://github.com/SocialGouv/code-du-travail-numerique/issues/7571)).
    - Stabilisation des jobs Playwright sur Ubuntu 24.04 ([#7568](https://github.com/SocialGouv/code-du-travail-numerique/issues/7568)) et correction du processus de publication npm ([#7579](https://github.com/SocialGouv/code-du-travail-numerique/issues/7579)).
- **Qualité et Observabilité** :
    - Initialisation du SDK Sentry côté serveur pour un meilleur suivi des erreurs ([#7578](https://github.com/SocialGouv/code-du-travail-numerique/issues/7578)).
    - Renforcement des tests E2E sur les dates des actualités et la robustesse des menus ([#7573](https://github.com/SocialGouv/code-du-travail-numerique/issues/7573)).
- **Maintenance** : Mise à jour des types des actualités via le package partagé ([#7570](https://github.com/SocialGouv/code-du-travail-numerique/issues/7570)).

### Autres changements
- **Documentation** : Création d'une checklist de validation SEO pour encadrer les changements ou suppressions d'URL ([#7581](https://github.com/SocialGouv/code-du-travail-numerique/issues/7581)).
