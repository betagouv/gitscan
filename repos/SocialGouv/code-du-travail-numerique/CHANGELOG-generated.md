## Changelog : code-du-travail-numerique (30 derniers jours, au 08/09/2026)

### Résumé
Cette période a été marquée par une amélioration de l'expérience utilisateur, notamment via la refonte du parcours de l'indemnité de précarité pour éviter les blocages et l'optimisation de la navigation (nouveau fil d'Ariane). Des corrections ont également été apportées pour améliorer le référencement (SEO) et la fiabilité des données analytiques de suivi.

### Évolutions fonctionnelles
- **Parcours utilisateur :**
  - Refonte complète du parcours de l'indemnité de précarité pour éliminer les points de blocage ([#7285](https://github.com/SocialGouv/code-du-travail-numerique/issues/7285)).
  - Ajout de liens vers des pages personnalisées dans la vue générique des contributions ([#7434](https://github.com/SocialGouv/code-du-travail-numerique/issues/7434)).
- **Navigation et SEO :**
  - Mise en place d'un nouveau fil d'Ariane pour les contenus natifs ([#7378](https://github.com/SocialGouv/code-du-travail-numerique/issues/7378), [#7443](https://github.com/SocialGouv/code-du-travail-numerique/issues/7443)).
  - Correction de la structure des titres (SEO) pour le NPS ([#7454](https://github.com/SocialGouv/code-du-travail-numerique/issues/7454)).
- **Corrections d'interface :**
  - Correction de la hiérarchie des titres et de leur taille dans les réponses des contributions ([#7468](https://github.com/SocialGouv/code-du-travail-numerique/issues/7468), [#7439](https://github.com/SocialGouv/code-du-travail-numerique/issues/7439), [#7440](https://github.com/SocialGouv/code-du-travail-numerique/issues/7440)).
  - Résolution d'un problème de bouton "Suivant" grisé lors du retour à l'étape Informations dans l'outil ([#7445](https://github.com/SocialGouv/code-du-travail-numerique/issues/7445)).

### Évolutions techniques
- **Analytique (Matomo) :**
  - Amélioration du suivi des données avec la mise en place d'un entonnoir (funnel) sur le choix de la convention collective des contributions ([#7463](https://github.com/SocialGouv/code-du-travail-numerique/issues/7463), [#7469](https://github.com/SocialGouv/code-du-travail-numerique/issues/7469)).
  - Ajout du suivi du nombre de conventions collectives trouvées ([#7428](https://github.com/SocialGouv/code-du-travail-numerique/issues/7428), [#7442](https://github.com/SocialGouv/code-du-travail-numerique/issues/7442)).
  - Correction d'un bug de perte de données lors de l'envoi d'événements analytiques ([#7449](https://github.com/SocialGouv/code-du-travail-numerique/issues/7449)).
