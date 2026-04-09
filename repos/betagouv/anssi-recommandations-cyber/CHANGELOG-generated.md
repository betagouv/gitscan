## Changelog : anssi-recommandations-cyber (30 derniers jours, au 08 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à l'interface d'interrogation du modèle IA Albert, alimenté par les guides de l'ANSSI. Les modifications récentes se concentrent sur l'amélioration de l'expérience utilisateur, la correction de problèmes de sécurité et la résolution de bugs mineurs.

### Évolutions fonctionnelles
- Amélioration du prompt utilisé par le modèle IA pour le rendre plus permissif et potentiellement améliorer la qualité des réponses.
- Affichage d'un lien "En savoir plus" lorsque la source documentaire est une page HTML, facilitant l'accès à l'information originale.
- Les collections de documents sont désormais affichées par ordre de création chronologique décroissant, permettant de visualiser les plus récentes en premier.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité : `dompurify`, `requests` et `svelte` (voir les alertes Dependabot [#58](https://github.com/betagouv/anssi-recommandations-cyber/security/dependabot/58), [#67](https://github.com/betagouv/anssi-recommandations-cyber/security/dependabot/67) et [#60](https://github.com/betagouv/anssi-recommandations-cyber/security/dependabot/60)).

### Autres changements
- Correction d'un bug où l'identifiant d'interaction envoyé à Metabase n'était pas chiffré, améliorant ainsi la confidentialité des données.
- Correction d'une faute de frappe dans la clé de la variable d'environnement du sel de hachage.
