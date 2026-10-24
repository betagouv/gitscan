## Changelog : translate-rt (30 derniers jours, au 14 octobre 2026)

### Résumé
Le projet a franchi une étape importante avec la publication de la version 0.2.0. Les récentes évolutions se sont concentrées sur l'amélioration significative de la rapidité de traitement de l'API et sur la mise en place d'une infrastructure de déploiement automatisée et robuste.

### Évolutions techniques
- **Optimisation de la performance et de la latence de l'API** :
  - Parallélisation des processus de transcription et de diarisation pour réduire le temps de traitement ([#4](https://github.com/IA-Generative/translate-rt/pull/4)).
  - Exécution simultanée des requêtes de traduction pour l'ensemble des cibles ([#5](https://github.com/IA-Generative/translate-rt/pull/5)).
  - Optimisation du flux de travail par le chevauchement (overlap) des étapes de traduction et de diarisation.
  - Amélioration de la réactivité du serveur en déportant la gestion des uploads vers un thread séparé, évitant ainsi de bloquer la boucle d'événements.
- **Infrastructure et Déploiement** :
  - Mise en place d'un environnement Docker et de pipelines CI/CD et DSO pour automatiser le déploiement CPiN ([#1](https://github.com/IA-Generative/translate-rt/pull/1)).

### Autres changements
- Publication de la version 0.2.0.
