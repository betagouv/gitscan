# mirai-mesreunions — fixtures audio

Échantillons audio de test pour [mirai-mesreunions](https://github.com/IA-Generative/mirai-mesreunions).
Sortis du repo principal pour ne pas alourdir son historique git.

Récupération depuis le repo principal : `deploy/scripts/setup.sh` les clone dans `tests/fixtures/audio/`.

## Contenu (`audio/`)
| Fichier | Origine | Usage |
|---|---|---|
| `eicar_test_virus.{mp3,wav}` | Chaîne de test antivirus EICAR (inoffensive) | Vérifier le scan ClamAV |
| `poemes01*_*.mp3` | LibriVox — **domaine public** | Transcription / diarisation |
| `test_audio_reunion_12s.mp3` | Snippet court de test | Smoke tests pipeline |
| `test_audio_voix_simulee.wav` | Voix synthétique | Tests de voix |

## Licences
- Poèmes : enregistrements LibriVox, **domaine public** (lecteurs : ezwa, chj, ng, jh).
- EICAR : chaîne de test standard, libre d'usage.
- Snippets de test : générés/synthétiques, sans contenu réel.
